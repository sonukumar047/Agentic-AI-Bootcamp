from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# -----------------------------------------
# 1. Load a text file
# -----------------------------------------
loader = TextLoader("data/sample.txt")
docs = loader.load()

# -----------------------------------------
# 2. Split into chunks
# -----------------------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(docs)

# -----------------------------------------
# 3. Initialize Ollama Embeddings (using nomic-embed-text)
# Pull it first: ollama pull nomic-embed-text
# -----------------------------------------
embedding = OllamaEmbeddings(model="nomic-embed-text")

# -----------------------------------------
# 4. Store chunks in FAISS
# -----------------------------------------
vectorstore = FAISS.from_documents(split_docs, embedding)

# -----------------------------------------
# 5. Perform a similarity search
# -----------------------------------------
query = "powerful programming language"
results = vectorstore.similarity_search(query, k=2)

# -----------------------------------------
# 6. Show Results
# -----------------------------------------
print("🔍 Similar Results:")
for i, doc in enumerate(results):
    print(f"\n🔹 Result {i+1}:\n{doc.page_content}")
