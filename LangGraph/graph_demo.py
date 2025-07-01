from langgraph.graph import END, StateGraph
from typing import TypedDict

# ✅ Define the shape of the shared state
class MyState(TypedDict):
    message: str

# ✅ Define your node functions
def greet(state: MyState) -> MyState:
    print("👋 Hello!")
    return {"message": "greeted"}

def ask_question(state: MyState) -> MyState:
    print("❓ How are you?")
    return {"message": "asked"}

def farewell(state: MyState) -> MyState:
    print("👋 Goodbye!")
    return {"message": "bye"}

# ✅ Create the graph with schema
graph = StateGraph(MyState)

graph.add_node("greet", greet)
graph.add_node("ask", ask_question)
graph.add_node("bye", farewell)

graph.set_entry_point("greet")
graph.add_edge("greet", "ask")
graph.add_edge("ask", "bye")
graph.add_edge("bye", END)

# ✅ Compile & Run
chain = graph.compile()
chain.invoke({"message": "start"})
