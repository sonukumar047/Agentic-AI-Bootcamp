from langchain_text_splitters import CharacterTextSplitter

text = "LangChain is awesome.\nIt makes LLM applications easier.\nThis is a simple demo."

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=30,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

print("📘 CharacterTextSplitter Output:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
