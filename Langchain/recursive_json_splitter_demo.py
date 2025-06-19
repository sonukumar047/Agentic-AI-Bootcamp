from langchain_text_splitters import RecursiveJsonSplitter
import json

# Sample nested JSON data
data = {
    "title": "LangChain JSON Example",
    "author": "Lang AI",
    "sections": [
        {
            "heading": "Introduction",
            "content": "LangChain is a framework for developing LLM applications."
        },
        {
            "heading": "Features",
            "content": "It supports chains, agents, memory, tools, and retrieval."
        },
        {
            "heading": "Use Cases",
            "content": "Chatbots, document search, and question answering are supported."
        }
    ],
    "metadata": {
        "version": 1.0,
        "created": "2024-06-01"
    }
}

# -----------------------------------------
# Initialize RecursiveJsonSplitter
# -----------------------------------------
splitter = RecursiveJsonSplitter(max_chunk_size=100)

# ✅ Correct Method: use `split_json()` instead of `split_text()`
chunks = splitter.split_json(json_data=data)

# -----------------------------------------
# Print the chunks
# -----------------------------------------
print("📘 Recursive JSON Text Splitter Output:\n")
for i, chunk in enumerate(chunks):
    print(f"🔹 Chunk {i+1}:")
    print(chunk)
    print("---")
