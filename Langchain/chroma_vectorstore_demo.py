from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# -----------------------------------------
# 1. Load text file
# -----------------------------------------
loader = TextLoader("data/sample.txt")
docs = loader.load()

# -----------------------------------------
# 2. Split into chunks
# -----------------------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(docs)

# -----------------------------------------
# 3. Create embeddings
# -----------------------------------------
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# -----------------------------------------
# 4. Create or load Chroma vector store
# No need to call .persist() anymore
# -----------------------------------------
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding,
    persist_directory="chroma_store"
)

# -----------------------------------------
# 5. Create retriever using .as_retriever()
# -----------------------------------------
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# -----------------------------------------
# 6. Use .invoke() instead of deprecated .get_relevant_documents()
# -----------------------------------------
query = "powerful programming language?"
docs = retriever.invoke(query)

# -----------------------------------------
# 7. Display the retrieved documents
# -----------------------------------------
print("\n🔍 Retrieved Documents:")
for i, doc in enumerate(docs):
    print(f"\n🔹 Result {i+1}:\n{doc.page_content}")

