import os
from dataclasses import dataclass, field
from typing import List
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
load_dotenv()
# -----------------------------------------
# 1. Define the State using @dataclass
# -----------------------------------------
@dataclass
class ChatState:
    username: str
    history: List[BaseMessage] = field(default_factory=list)

# -----------------------------------------
# 2. Set your GROQ API key
# -----------------------------------------
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  # Replace with your real key

# -----------------------------------------
# 3. Node Function: Handle a conversation step
# -----------------------------------------
def groq_chat(state: ChatState, config: RunnableConfig = None) -> ChatState:
    llm = ChatGroq(
        model="llama3-8b-8192",
        api_key=os.environ["GROQ_API_KEY"]
    )

    response = llm.invoke(state.history)
    print(f"\n🤖 {state.username}, Bot says: {response.content}")

    # Update state with new AI response
    state.history.append(AIMessage(content=response.content))
    return state

# -----------------------------------------
# 4. Build LangGraph with the State
# -----------------------------------------
graph = StateGraph(ChatState)
graph.add_node("groq_chat", groq_chat)
graph.set_entry_point("groq_chat")
graph.add_edge("groq_chat", END)
chatbot = graph.compile()

# -----------------------------------------
# 5. Chat Loop
# -----------------------------------------
if __name__ == "__main__":
    print("💬 LangGraph Chatbot with Dataclass State (type 'exit' to quit)")
    name = input("👤 Enter your name: ")
    state = ChatState(username=name)

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        # Add user input to chat history
        state.history.append(HumanMessage(content=user_input))

        # Run the graph
        new_state = chatbot.invoke(state)

        # Ensure state is still a ChatState object
        if isinstance(new_state, dict):
            state = ChatState(**new_state)
        else:
            state = new_state
