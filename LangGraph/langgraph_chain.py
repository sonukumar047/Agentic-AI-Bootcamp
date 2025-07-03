# langgraph_chain.py
from dataclasses import dataclass, field
from typing import List
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import END, StateGraph
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

# 1️⃣ Set API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  # 🔁 Replace

# ---------------------------------------
# 1. Define the state using a dataclass
# ---------------------------------------
@dataclass
class ChatState:
    history: List[BaseMessage] = field(default_factory=list)

# ---------------------------------------
# 2. Define LLM Node
# ---------------------------------------
def chat_node(state: ChatState) -> ChatState:
    llm = ChatGroq(model="llama3-8b-8192", api_key=os.environ["GROQ_API_KEY"])

    response = llm.invoke(state.history)
    print(f"\n🤖 Bot: {response.content}")

    return ChatState(history=state.history + [AIMessage(content=response.content)])

# ---------------------------------------
# 3. Build Graph
# ---------------------------------------
graph = StateGraph(ChatState)
graph.add_node("chat", chat_node)
graph.set_entry_point("chat")
graph.add_edge("chat", END)
chatbot = graph.compile()

# ---------------------------------------
# 4. Run
# ---------------------------------------
if __name__ == "__main__":
    state = ChatState()
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        state.history.append(HumanMessage(content=user_input))
        output = chatbot.invoke(state)
        state = ChatState(**output)



