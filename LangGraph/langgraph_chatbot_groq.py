import os
from typing import Annotated
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END

# -----------------------------------------
# Define your own add_messages helper
# -----------------------------------------
def add_messages(messages: list, new_messages: list) -> list:
    return messages + new_messages

ChatState = Annotated[list, add_messages]

# -----------------------------------------
# Set your GROQ API key
# -----------------------------------------
# os.environ["GROQ_API_KEY"] = "Groq API KEY"  # Replace this

# -----------------------------------------
# Node: Groq-powered chat function
# -----------------------------------------
def groq_chat(messages: ChatState) -> ChatState:
    llm = ChatGroq(
        model="llama3-8b-8192",
        api_key=os.environ["GROQ_API_KEY"]
    )
    response = llm.invoke(messages)
    print(f"\n🤖 Bot: {response.content}")
    return [AIMessage(content=response.content)]

# -----------------------------------------
# Build the graph
# -----------------------------------------
graph = StateGraph(ChatState)
graph.add_node("groq_chat", groq_chat)
graph.set_entry_point("groq_chat")
graph.add_edge("groq_chat", END)
chatbot = graph.compile()

# -----------------------------------------
# Run the looped chatbot
# -----------------------------------------
if __name__ == "__main__":
    print("🧠 LangGraph + Groq Chatbot (Type 'exit' to quit)\n")
    state = []

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        state.append(HumanMessage(content=user_input))
        state = chatbot.invoke(state)