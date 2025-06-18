from langchain_text_splitters import HTMLHeaderTextSplitter

# Sample HTML content
html_text = """
<html>
  <body>
    <h1>LangChain Overview</h1>
    <p>LangChain is a framework for building LLM-powered applications.</p>
    
    <h2>Components</h2>
    <p>There are several components including Chains, Agents, Tools, and Memory.</p>
    
    <h2>Use Cases</h2>
    <p>LangChain can be used for chatbots, data QA, summarization, and more.</p>
    
    <h3>Chatbots</h3>
    <p>You can create conversational bots with context memory.</p>
    
    <h3>Summarization</h3>
    <p>Summarize long articles or documents into concise summaries.</p>
  </body>
</html>
"""

# Define header tags to split on
headers_to_split_on = [
    ("h1", "Heading 1"),
    ("h2", "Heading 2"),
    ("h3", "Heading 3")
]

# Initialize the HTML Header Splitter
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

# Split the HTML
docs = html_splitter.split_text(html_text)

# Output the results
print("📘 HTML Header Text Splitter Output:\n")
for i, doc in enumerate(docs):
    print(f"🔹 Chunk {i+1}:")
    print(doc.page_content)
    print("---")
