from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM  # ✅ from langchain_ollama not langchain_community


# -----------------------------------------
# 1. Initialize the LLM
# -----------------------------------------
llm = OllamaLLM(model="llama3.2:3b")

# -----------------------------------------
# 2. Prompt Template
# -----------------------------------------
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms like I am five years old."
)

# -----------------------------------------
# 3. Output Parser
# -----------------------------------------
parser = StrOutputParser()

# -----------------------------------------
# 4. Create the Chain (new syntax using `|`)
# -----------------------------------------
chain = prompt | llm | parser

# -----------------------------------------
# 5. Invoke the Chain
# -----------------------------------------
response = chain.invoke({"topic": "quantum computing"})

# -----------------------------------------
# 6. Print the Output
# -----------------------------------------
print("\n📘 LLM Output:")
print(response)


# -----------------------------------------
# Summary of Components Used:
# - LLM: `Ollama` (used to talk to LLMs)
# - PromptTemplate: Used to format user input
# - LLMChain: Wraps LLM and prompt into a pipeline
# - OutputParser: Cleanly formats the result
# -----------------------------------------