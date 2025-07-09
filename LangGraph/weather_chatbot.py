import os
import re
import requests
from dataclasses import dataclass, field
from typing import List

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import tool

load_dotenv()

# -------------------------------
# 🔐 Set API keys
# -------------------------------
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# -------------------------------
# 🧰 Real-time Weather Tool
# -------------------------------
@tool
def get_weather(location: str) -> str:
    """Fetches real-time weather for a location using OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()
        if res.status_code != 200 or "main" not in data:
            return f"⚠️ Could not fetch weather for '{location}'. Please check spelling."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"🌤️ {location.title()}: {temp}°C, {desc}"
    except Exception as e:
        return f"❌ Error fetching weather: {str(e)}"

# -------------------------------
# 🧠 Define Chat State
# -------------------------------
@dataclass
class ChatState:
    history: List[BaseMessage] = field(default_factory=list)

# -------------------------------
# 🤖 Chat Node with Weather Logic
# -------------------------------
def chat_node(state: ChatState) -> ChatState:
    llm = ChatGroq(model="llama3-8b-8192", api_key=os.environ["GROQ_API_KEY"])

    last_input = state.history[-1].content.lower()

    # Check if it's a weather-related query
    is_weather_query = any(word in last_input for word in ["weather", "temperature", "climate", "hot", "cold", "raining"])
    location_match = re.search(r"(?:in|of)\s+([a-zA-Z\s]+)", last_input)
    location = location_match.group(1).strip() if location_match else None

    if is_weather_query and location:
        weather_info = get_weather.invoke(location)
        ai_message = AIMessage(content=weather_info)
    else:
        response = llm.invoke(state.history)
        ai_message = AIMessage(content=response.content or "❓ I didn't understand. Can you rephrase?")

    print(f"\n🤖 Bot: {ai_message.content}")
    return ChatState(history=state.history + [ai_message])

# -------------------------------
# 🔗 Build LangGraph
# -------------------------------
graph_builder = StateGraph(ChatState)
graph_builder.add_node("chat", chat_node)
graph_builder.set_entry_point("chat")
graph_builder.add_edge("chat", END)
graph = graph_builder.compile()

# -------------------------------
# 🏁 Chat Loop
# -------------------------------
if __name__ == "__main__":
    state = ChatState()

    while True:
        user_input = input("👤 You: ")
        if user_input.lower().strip() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        state.history.append(HumanMessage(content=user_input))
        result = graph.invoke(state)

        # ✅ Ensure we get back a ChatState object
        if isinstance(result, dict):
            state = ChatState(**result)
        else:
            state = result
