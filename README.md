# LangChain Project

This project demonstrates the use of LangChain for various tasks such as document loading, text splitting, vector indexing, and retrieval-based question answering. The project is implemented using Python and integrates with the Mistral AI model.

## Project Structure

```
.
├── .env
├── .gitignore
├── .vscode/
│   ├── launch.json
├── analysis1.pk1
├── equity_research.ipynb
├── faiss_store/
│   ├── index.faiss
│   ├── index.pkl
├── LandChain.ipynb
├── langchain_helper.py
├── LangChainInvester.ipynb
├── main.py
├── my_secret_key.py
├── RAG.ipynb
├── requirments.txt
├── restaurant_menu_finder.py
├── retrieval.ipynb
├── sample.csv
├── sample.txt
├── test.py
├── vector_index.pk1/
│   ├── index.faiss
│   ├── index.pkl
├── vector_index.pkl
├── vector.csv
├── vectors.ipynb
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirments.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   MISTRAL_API_KEY="your_mistral_api_key"
   OPENAI_API_KEY="your_openai_api_key"
   GOOGLE_API_KEY="your_google_api_key"
   ```

## Usage

### Running Notebooks

- **LangChainInvester.ipynb**: Demonstrates loading CSV data and extracting metadata.
- **equity_research.ipynb**: Shows how to load data from URLs, split text into chunks, create embeddings, and perform retrieval-based QA.
- **RAG.ipynb**: Implements a retrieval-augmented generation pipeline using SQL databases.
- **retrieval.ipynb**: Demonstrates loading data, splitting text, creating embeddings, and retrieving answers using FAISS index.
- **vectors.ipynb**: Shows how to load vector data, create embeddings, and use FAISS for vector indexing.

### Running Scripts

- **main.py**: Streamlit application for processing news articles and performing research tasks.
  ```sh
  streamlit run main.py
  ```

- **restaurant_menu_finder.py**: Streamlit application for generating restaurant names and menu items.
  ```sh
  streamlit run restaurant_menu_finder.py
  ```

- **test.py**: Script for testing LangChain functionalities such as generating play synopses and reviews.
  ```sh
  python test.py
  ```

## Helper Functions

- **langchain_helper.py**: Contains helper functions for generating restaurant names and menu items using LangChain.

## Data Files

- **sample.csv**: Sample CSV file used in the notebooks.
- **sample.txt**: Sample text file used in the notebooks.
- **vector.csv**: Sample vector data used in the notebooks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the notebooks and scripts to understand how LangChain can be used for various NLP tasks. If you have any questions or issues, please open an issue in the repository.