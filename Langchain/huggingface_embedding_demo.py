from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# -----------------------------------------
# 1. Load your document
# -----------------------------------------
loader = TextLoader("data/sample.txt")
docs = loader.load()

# -----------------------------------------
# 2. Split text into chunks
# -----------------------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(docs)

# -----------------------------------------
# 3. Use a local Hugging Face embedding model
# Recommended: all-MiniLM-L6-v2 (fast and small)
# -----------------------------------------
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding = HuggingFaceEmbeddings(model_name=embedding_model_name)

# -----------------------------------------
# 4. Store embeddings in FAISS
# -----------------------------------------
vectorstore = FAISS.from_documents(split_docs, embedding)

# -----------------------------------------
# 5. Perform similarity search
# -----------------------------------------
query = "powerful programming language?"
results = vectorstore.similarity_search(query, k=2)

# -----------------------------------------
# 6. Show the best matches
# -----------------------------------------
print("🔍 Similar Results:")
for i, doc in enumerate(results):
    print(f"\n🔹 Result {i+1}:\n{doc.page_content}")
