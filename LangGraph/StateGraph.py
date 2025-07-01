# StateGraph.py

from langgraph.graph import StateGraph, END
from typing import TypedDict

# ✅ Define state schema
class MyState(TypedDict):
    number: int
    next: str

# ✅ Step 1: Define shared state functions
def check_even_odd(state: MyState) -> MyState:
    number = state["number"]
    if number % 2 == 0:
        print(f"{number} is even")
        return {"number": number, "next": "even"}
    else:
        print(f"{number} is odd")
        return {"number": number, "next": "odd"}

def handle_even(state: MyState) -> MyState:
    print("Handling even...")
    return state

def handle_odd(state: MyState) -> MyState:
    print("Handling odd...")
    return state

# ✅ Step 2: Create StateGraph with schema
graph = StateGraph(MyState)

graph.add_node("checker", check_even_odd)
graph.add_node("even", handle_even)
graph.add_node("odd", handle_odd)

graph.set_entry_point("checker")
graph.add_conditional_edges("checker", lambda x: x["next"], {
    "even": "even",
    "odd": "odd"
})

graph.add_edge("even", END)
graph.add_edge("odd", END)

# ✅ Step 3: Compile and run
chain = graph.compile()
chain.invoke({"number": 5, "next": ""})
