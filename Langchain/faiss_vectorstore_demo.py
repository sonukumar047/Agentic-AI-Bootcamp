from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# -----------------------------------------
# 1. Load a document
# -----------------------------------------
loader = TextLoader("data/sample.txt")
docs = loader.load()

# -----------------------------------------
# 2. Split text into chunks
# -----------------------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(docs)

# -----------------------------------------
# 3. Create embeddings (local HF example)
# -----------------------------------------
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# -----------------------------------------
# 4. Store chunks in FAISS vector store
# -----------------------------------------
vectorstore = FAISS.from_documents(split_docs, embedding)

# ✅ Save the vectorstore to disk
vectorstore.save_local("faiss_index")

# -----------------------------------------
# 5. Load vectorstore from disk later (if needed)
# -----------------------------------------
# vectorstore = FAISS.load_local("faiss_index", embedding)

# -----------------------------------------
# 6. Perform similarity search
# -----------------------------------------
query = "powerful programming language?"
results = vectorstore.similarity_search(query, k=2)

# -----------------------------------------
# 7. Show results
# -----------------------------------------
print("🔍 FAISS Similar Results:")
for i, doc in enumerate(results):
    print(f"\n🔹 Result {i+1}:\n{doc.page_content}")
