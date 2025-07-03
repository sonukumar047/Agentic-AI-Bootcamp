import os
from dataclasses import dataclass, field
from typing import List
import re

from langgraph.graph import StateGraph, END
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# -------------------------------
# ✅ Tool: add two numbers
# -------------------------------
@tool
def add_numbers(a: int, b: int) -> str:
    """Adds two integers."""
    return f"✅ The sum of {a} and {b} is {a + b}"

# -------------------------------
# ✅ State class
# -------------------------------
@dataclass
class ChatState:
    history: List[BaseMessage] = field(default_factory=list)

# -------------------------------
# ✅ Node: processing logic
# -------------------------------
def add_node(state: ChatState) -> ChatState:
    try:
        last_input = state.history[-1].content.lower()
        numbers = re.findall(r"\d+", last_input)

        if len(numbers) < 2:
            reply = "❌ Please provide two numbers like: 'add 3 and 5'."
        else:
            a, b = int(numbers[0]), int(numbers[1])
            reply = add_numbers.invoke({"a": a, "b": b})
    except Exception as e:
        reply = f"❌ An error occurred: {e}"

    print(f"\n🤖 Bot: {reply}")
    return ChatState(history=state.history + [AIMessage(content=reply)])

# -------------------------------
# ✅ LangGraph wiring
# -------------------------------
graph = StateGraph(ChatState)
graph.add_node("add", add_node)
graph.set_entry_point("add")
graph.add_edge("add", END)
chatbot = graph.compile()

# -------------------------------
# ✅ Chat loop
# -------------------------------
if __name__ == "__main__":
    state = ChatState()

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        state.history.append(HumanMessage(content=user_input))
        result = chatbot.invoke(state)

        # 🛠️ Reassign state only if result is valid
        if isinstance(result, ChatState):
            state = result
        else:
            print("⚠️ Unexpected result from graph. Resetting state.")
            state = ChatState()
