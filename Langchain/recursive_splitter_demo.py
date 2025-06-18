from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample large text
text = """
Artificial Intelligence (AI) is transforming industries across the globe.
From healthcare to finance, AI algorithms are now capable of performing tasks
that were once thought to be exclusive to humans. These include understanding
natural language, recognizing images, and making complex decisions. However,
AI is not without its limitations and ethical concerns, especially regarding
bias and privacy.
"""

# -----------------------------------------
# Initialize RecursiveCharacterTextSplitter
# -----------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", ".", " ", ""]
)

# -----------------------------------------
# Split the document into chunks
# -----------------------------------------
chunks = text_splitter.split_text(text)

# -----------------------------------------
# Display chunks
# -----------------------------------------
print("📚 Total Chunks:", len(chunks))
for i, chunk in enumerate(chunks):
    print(f"\n🔹 Chunk {i+1}:\n{chunk}")
