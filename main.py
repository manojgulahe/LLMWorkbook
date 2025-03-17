import os
import streamlit as st
import pickle
import time
from langchain_mistralai import ChatMistralAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from my_secret_key import mistral_key
from dotenv import load_dotenv

#os.environ["MISTRAL_API_KEY"]=mistral_key
load_dotenv() #take a variable from .env file

# print(os.getenv("MISTRAL_API_KEY"))
st.title("News Research Tools")
st.sidebar.title("News articles URLs")

urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"Url {i+1}")
    urls.append(url)
process_clicked =st.sidebar.button("Process URLs")
FILE_PATH="faiss_store"

main_placeholder=st.empty()
llm  = ChatMistralAI(model="mistral-large-latest")

if process_clicked:  
    main_placeholder.text("loading data")
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    # split data
    main_placeholder.text("splitting data")
    # splitter = RecursiveCharacterTextSplitter(separators=["\n\n","\n"," "],
    #                                chunk_size=500)
    # text_splitter = RecursiveCharacterTextSplitter(
    # chunk_size=1000,
    # chunk_overlap=200)
    splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    docs=splitter.split_documents(data)
    # create embedding
    main_placeholder.text("embedding data")

    if(not os.path.exists(FILE_PATH)):
         # tokenizer='mistral-embed'
        embedding = MistralAIEmbeddings()
        # len(embedding)
        vectors = FAISS.from_documents(docs,embedding)
        time.sleep(2)
         # Save the FAISS index to a pickle file
        # with open(FILE_PATH, "wb") as f:
        #     pickle.dump(vectors, f)
        vectors.save_local(FILE_PATH)

query = main_placeholder.text_input("question:")
if len(query) > 0 and os.path.exists(FILE_PATH):
    vectorstore=FAISS.load_local(FILE_PATH,MistralAIEmbeddings(),allow_dangerous_deserialization=True)
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vectorstore.as_retriever())
    print("started")
    result = chain({"question":query},return_only_outputs=True)
    print("ended")
    st.header("Answer:")
    st.subheader(result["answer"])
