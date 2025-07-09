import os
import streamlit as st
from typing import List, Dict, Any, TypedDict, Annotated
from dotenv import load_dotenv

# LangChain/LangGraph imports
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, ToolMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages

# Load environment variables from .env file
load_dotenv()

# --- Tools Definition ---

@tool
def get_faq_answer(query: str) -> str:
    """Provides answers to frequently asked questions about product features, billing, or common issues.
    Input: The specific question about a product or service.
    Output: The answer to the FAQ or a message indicating the question is not in the FAQ.
    """
    st.info(f"Executing tool: get_faq_answer with query: '{query}'")
    faqs = {
        "how to reset password": "You can reset your password by visiting our login page and clicking 'Forgot Password'. Follow the instructions sent to your registered email.",
        "what is your refund policy": "Our refund policy allows for a full refund within 30 days of purchase, provided the service has not been extensively used. Please refer to our terms and conditions for more details.",
        "how to contact support": "You can contact support via email at support@example.com or call us at 1-800-555-1234 during business hours (9 AM - 5 PM EST, Mon-Fri).",
        "what are your pricing plans": "We offer various pricing plans including Basic, Pro, and Enterprise. Details can be found on our pricing page or by contacting our sales team.",
        "how to upgrade my account": "To upgrade your account, navigate to your account settings or dashboard, and look for the 'Upgrade Plan' option. Follow the prompts to select a new plan."
    }
    # Simple keyword matching for demo purposes
    for key, value in faqs.items():
        if key in query.lower():
            return value
    return "I'm sorry, I couldn't find an answer to that in our FAQs. Would you like me to escalate this to a human agent?"

@tool
def escalate_to_human_agent(reason: str) -> str:
    """Escalates the current customer query to a human support agent.
    This tool should be used when the automated agent cannot resolve the query.
    Input: A brief reason for escalation.
    Output: A confirmation message that the query has been escalated.
    """
    st.info(f"Executing tool: escalate_to_human_agent with reason: '{reason}'")
    return f"Your request has been escalated to a human agent. Reason: '{reason}'. A support representative will contact you shortly."

# List of all available tools
tools = [get_faq_answer, escalate_to_human_agent]

# --- LangGraph State Definition ---
# This defines the state that will be passed between nodes in the graph.
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    intermediate_steps: List[Dict[str, Any]] # For UI display of ReAct steps

# --- LangGraph Nodes ---

def call_llm_and_decide_action(state: AgentState) -> Dict[str, Any]:
    """
    Invokes the LLM to decide the next action: use a tool or provide a final answer.
    """
    st.markdown("--- **Agent Thinking** ---")
    st.markdown("🤖 Calling LLM for decision...")

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY environment variable not set. Please set it in your .env file.")
        raise ValueError("GROQ_API_KEY environment variable not set.")
        
    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful customer support agent. Your goal is to assist users with their queries.
         You have access to the following tools:
         {tools}
         
         - Use 'get_faq_answer' when the user asks a question that might be covered in our frequently asked questions.
         - Use 'escalate_to_human_agent' if you cannot find an answer in the FAQs or if the user explicitly asks to speak to a human.
         
         If you need to use a tool, output a tool call.
         If you have enough information to answer the user's query directly, provide the final answer.
         Do NOT include "Thought:", "Action:", "Tool:", "Tool_Input:", "Answer:" in your final response content.
         Just provide the answer or the tool call.
         """),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]).partial(tools="\n".join([f"{t.name}: {t.description}" for t in tools]))

    llm_with_tools = llm.bind_tools(tools)
    agent_runnable = prompt | llm_with_tools

    # Construct llm_scratchpad from messages for the LLM
    llm_scratchpad = []
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            llm_scratchpad.append(msg)
        elif isinstance(msg, ToolMessage):
            llm_scratchpad.append(msg)

    response = agent_runnable.invoke({
        "messages": state["messages"], 
        "agent_scratchpad": llm_scratchpad
    })

    new_intermediate_steps = list(state["intermediate_steps"])
    
    thought_text = ""
    action_type = "final_answer"
    tool_name = None
    tool_input = None

    if response.tool_calls:
        action_type = "tool_code"
        tool_call = response.tool_calls[0]
        tool_name = tool_call['name']
        tool_input = tool_call['args']
        thought_text = f"I need to use the '{tool_name}' tool." 
    else:
        thought_text = "I have enough information to provide a final answer."

    new_intermediate_steps.append({
        "type": "thought_action",
        "thought": thought_text,
        "action": action_type,
        "tool_name": tool_name,
        "tool_input": tool_input
    })

    return {"messages": [response], "intermediate_steps": new_intermediate_steps}

def execute_tools(state: AgentState) -> Dict[str, Any]:
    """
    Executes the tool called by the LLM.
    """
    st.markdown("--- **Tool Execution** ---")
    st.markdown("🛠️ Executing Tools...")
    last_message = state["messages"][-1]
    tool_outputs = []
    new_intermediate_steps = list(state["intermediate_steps"])

    tool_map = {tool.name: tool for tool in tools}

    for tool_call in last_message.tool_calls:
        tool_name = tool_call['name']
        tool_args = tool_call['args']
        
        if tool_name in tool_map:
            selected_tool = tool_map[tool_name]
            try:
                output = selected_tool.invoke(tool_args)
                tool_outputs.append(ToolMessage(content=str(output), tool_call_id=tool_call['id']))
                st.markdown(f"**Observation:** {str(output)}")
                
                new_intermediate_steps.append({
                    "type": "observation",
                    "observation": str(output)
                })
            except Exception as e:
                error_message = f"Tool '{tool_name}' failed: {e}"
                tool_outputs.append(ToolMessage(content=error_message, tool_call_id=tool_call['id']))
                st.error(f"**Observation (Error):** {error_message}")
                
                new_intermediate_steps.append({
                    "type": "observation",
                    "observation": error_message
                })
        else:
            error_message = f"Tool '{tool_name}' not found."
            tool_outputs.append(ToolMessage(content=error_message, tool_call_id=tool_call['id']))
            st.error(f"**Observation (Error):** {error_message}")
            new_intermediate_steps.append({
                "type": "observation",
                "observation": error_message
            })

    return {"messages": tool_outputs, "intermediate_steps": new_intermediate_steps}

# --- LangGraph Graph Definition ---

workflow = StateGraph(AgentState)

workflow.add_node("decide_action", call_llm_and_decide_action)
workflow.add_node("execute_tools", execute_tools)

workflow.set_entry_point("decide_action")

workflow.add_conditional_edges(
    "decide_action",
    lambda state: "execute_tools" if state["messages"][-1].tool_calls else END,
    {
        "execute_tools": "execute_tools",
        END: END
    }
)

workflow.add_edge("execute_tools", "decide_action")

app_graph = workflow.compile()

# --- Streamlit UI ---

st.set_page_config(page_title="Customer Support Agent (LangGraph Studio Example)", layout="centered")

st.title("📞 Customer Support Agent")
st.markdown("I can help with FAQs or escalate your query to a human agent.")
st.markdown("""
**Try asking:**
- "How do I reset my password?"
- "What is your refund policy?"
- "How can I contact support?"
- "I need to talk to a human agent about a complex issue."
- "What are your pricing plans?"
""")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "intermediate_steps" not in st.session_state:
    st.session_state.intermediate_steps = []

# Display chat messages from history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)
    elif isinstance(msg, ToolMessage):
        st.chat_message("assistant").write(f"Tool Output: {msg.content}")

# Chat input
user_input = st.chat_input("Your question:")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    with st.spinner("Agent is thinking..."):
        try:
            st.session_state.intermediate_steps = []
            
            initial_graph_state = {
                "messages": [HumanMessage(content=user_input)],
                "intermediate_steps": []
            }

            final_graph_state = app_graph.invoke(initial_graph_state)

            user_msg_index = -1
            for i, msg in enumerate(final_graph_state["messages"]):
                if isinstance(msg, HumanMessage) and msg.content == user_input:
                    user_msg_index = i
                    break
            
            if user_msg_index != -1:
                new_agent_messages_from_graph = final_graph_state["messages"][user_msg_index+1:]
            else:
                new_agent_messages_from_graph = final_graph_state["messages"]

            for msg in new_agent_messages_from_graph:
                if isinstance(msg, AIMessage):
                    st.session_state.messages.append(msg)
                elif isinstance(msg, ToolMessage):
                    pass 

            st.session_state.intermediate_steps.extend(final_graph_state["intermediate_steps"])

            final_answer_to_display = "I couldn't generate a final answer. Please try again."
            for msg in reversed(st.session_state.messages):
                if isinstance(msg, AIMessage) and msg.content:
                    final_answer_to_display = msg.content
                    break
            
            if final_answer_to_display != "I couldn't generate a final answer. Please try again.":
                st.chat_message("assistant").write(final_answer_to_display)
            else:
                st.chat_message("assistant").write("I couldn't generate a final answer. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.messages.append(AIMessage(content=f"An error occurred: {e}"))

# Display intermediate steps for debugging/visualization
if st.session_state.intermediate_steps:
    st.sidebar.title("ReAct Process Steps")
    for step in st.session_state.intermediate_steps:
        if step["type"] == "thought_action":
            st.sidebar.markdown(f"**Thought:** {step['thought']}")
            st.sidebar.markdown(f"**Action:** {step['action']}")
            if step["tool_name"]:
                st.sidebar.markdown(f"**Tool:** `{step['tool_name']}`")
                st.sidebar.markdown(f"**Tool Input:** `{step['tool_input']}`")
        elif step["type"] == "observation":
            st.sidebar.markdown(f"**Observation:** {step['observation']}")
        st.sidebar.markdown("---")
