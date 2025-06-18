# data_ingestion_demo.py

from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader, DirectoryLoader
from pathlib import Path

# -----------------------------------------
# 1. PDF Loader
# -----------------------------------------
# from fpdf import FPDF

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.multi_cell(0, 10, "LangChain is amazing!\n\nIt helps integrate language models into your apps.\n\nThis PDF is for testing document loaders.")
# pdf.output("D:/Agentic-AI-Bootcamp/data/sample.pdf")
# print("✅ sample.pdf created successfully.")

pdf_path = "data/sample.pdf"  # 🔁 Replace with your file path
pdf_loader = PyPDFLoader(pdf_path)
pdf_docs = pdf_loader.load()
print(f"\n📄 PDF Loaded: {len(pdf_docs)} pages")

# -----------------------------------------
# 2. Text File Loader
# -----------------------------------------
txt_loader = TextLoader("data/sample.txt")
txt_docs = txt_loader.load()
print(f"\n📄 Text File Loaded: {len(txt_docs)} document")

# -----------------------------------------
# 3. CSV Loader
# -----------------------------------------
csv_loader = CSVLoader(file_path="data/sample.csv")
csv_docs = csv_loader.load()
print(f"\n📊 CSV Loaded: {len(csv_docs)} rows")

# -----------------------------------------
# 4. Directory Loader (load all files)
# -----------------------------------------
folder_loader = DirectoryLoader("data/", glob="**/*.txt", loader_cls=TextLoader)
folder_docs = folder_loader.load()
print(f"\n📁 Folder Loaded: {len(folder_docs)} text files")

# -----------------------------------------
# View sample content
# -----------------------------------------
print("\n📌 Sample Document Content (from PDF):")
print(pdf_docs[0].page_content[:300])
