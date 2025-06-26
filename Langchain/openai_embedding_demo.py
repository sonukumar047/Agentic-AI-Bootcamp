from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

# ✅ Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxx"

# -----------------------------------------
# 1. Load a sample text file
# -----------------------------------------
loader = TextLoader("data/sample.txt")
docs = loader.load()

# -----------------------------------------
# 2. Split the documents into chunks
# -----------------------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(docs)

# -----------------------------------------
# 3. Initialize OpenAI Embeddings
# -----------------------------------------
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# -----------------------------------------
# 4. Store in FAISS vector store
# -----------------------------------------
vectorstore = FAISS.from_documents(split_docs, embedding)

# -----------------------------------------
# 5. Perform a similarity search
# -----------------------------------------
query = "What is LangChain?"
results = vectorstore.similarity_search(query)

# -----------------------------------------
# 6. Print the best match
# -----------------------------------------
print("🔍 Top Match:\n")
print(results[0].page_content)
