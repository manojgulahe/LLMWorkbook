from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI
from my_secret_key import mistral_key
import os
os.environ["MISTRAL_API_KEY"] = mistral_key

def generate_restaurant_name_items(cuisine):
    model = ChatMistralAI(model="mistral-large-latest")
    parser = StrOutputParser()
    p1=PromptTemplate(input_variables=['cuisine'],template="I want to open restaturant for {cuisine} food.Suggest only one fancy name for this. Respond only name")
    p2=PromptTemplate(input_variables=['restaurant_name'],template="Suggest some menu items for {restaurant_name}. Return only menu item names in comma seprated list")

    # Create chains for generating restaurant names and menu items
    name_chain = LLMChain(prompt=p1, llm=model, output_parser=parser,output_key='restaurant_name')
    menu_chain = LLMChain(prompt=p2, llm=model, output_parser=parser,output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items'],
        verbose=True
    )

    menu_items = chain({'cuisine':'italian'})
    print("==========",menu_items)
    return menu_items

if __name__ == "__main__":
    print(generate_restaurant_name_items("italian"))
