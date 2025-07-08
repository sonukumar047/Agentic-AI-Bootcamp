# streamlit_app.py
import os
import streamlit as st
from dotenv import load_dotenv
from typing import List, Dict, Any, TypedDict, Annotated # Import TypedDict and Annotated

# LangChain/LangGraph imports
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, ToolMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, END
# Import add_messages for state annotation
from langgraph.graph.message import add_messages 

# Load environment variables from .env file
load_dotenv()

# --- Tools Definition ---

@tool
def recommend_resources(domain: str) -> str:
    """Suggests learning resources for a specific career domain.
    Input: The career domain (e.g., 'AI Engineering', 'Data Science').
    Output: A string containing YouTube, GitHub, and blog resources.
    """
    st.info(f"Executing tool: recommend_resources with domain: {domain}")
    return f"""📘 Learn {domain}:
- YouTube: 'Learn {domain} in 10 Hours'
- GitHub: https://github.com/awesome-{domain.lower().replace(' ', '-')}-resources
- Blog: https://roadmap.sh/{domain.lower().replace(' ', '-')}-roadmap"""

@tool
def generate_roadmap(domain: str) -> str:
    """Generates a structured roadmap for the given career domain.
    Input: The career domain (e.g., 'Web Development', 'Cybersecurity').
    Output: A string outlining a 5-step career roadmap.
    """
    st.info(f"Executing tool: generate_roadmap with domain: {domain}")
    return f"""🧭 {domain} Roadmap:
1. Learn Fundamentals: Master core concepts and theories.
2. Master Tools & Technologies: Become proficient with essential software and frameworks.
3. Build Projects: Apply knowledge by creating practical projects.
4. Update Resume & Portfolio: Showcase your skills and experience effectively.
5. Prepare for Interviews: Practice technical and behavioral questions."""

@tool
def career_outlook(domain: str) -> str:
    """Provides a general job market outlook and salary information for a specific career domain.
    Input: The career domain (e.g., 'Software Engineering', 'Marketing').
    Output: A string with outlook and salary estimates.
    """
    st.info(f"Executing tool: career_outlook with domain: {domain}")
    outlooks = {
        "data science": "The job outlook for Data Scientists is excellent, projected to grow 35% from 2022 to 2032. Median salary is around $103,500 per year.",
        "web development": "Web Developer jobs are expected to grow 16% from 2022 to 2032. Median salary is about $80,730 per year.",
        "ai engineering": "AI Engineering is a rapidly growing field with high demand. While specific statistics are emerging, growth is expected to be very strong. Salaries are typically high, often exceeding $120,000 per year.",
        "cybersecurity": "Cybersecurity Analyst jobs are projected to grow 32% from 2022 to 2032. Median salary is around $120,360 per year.",
        "software engineering": "Software Developer jobs are projected to grow 25% from 2022 to 2032. Median salary is around $124,200 per year."
    }
    return outlooks.get(domain.lower(), f"No specific outlook data for {domain}. Generally, tech roles are in high demand.")

@tool
def interview_tips(role: str) -> str:
    """Provides general interview tips for a specific job role.
    Input: The job role (e.g., 'Data Scientist', 'Software Engineer').
    Output: A string with key interview preparation advice.
    """
    st.info(f"Executing tool: interview_tips for role: {role}")
    tips = {
        "data scientist": """Interview Tips for Data Scientist:
1. Master statistics and probability.
2. Practice SQL and Python/R coding (Pandas, NumPy, Scikit-learn).
3. Understand machine learning algorithms and their applications.
4. Prepare for case studies and behavioral questions.
5. Be ready to discuss your projects and problem-solving approach.""",
        "software engineer": """Interview Tips for Software Engineer:
1. Practice data structures and algorithms (LeetCode is great).
2. Understand core computer science fundamentals (OS, Networking, Databases).
3. Be proficient in at least one programming language (Java, Python, C++).
4. Prepare for system design questions.
5. Focus on clear communication during technical discussions.""",
        "web developer": """Interview Tips for Web Developer:
1. Solid understanding of HTML, CSS, JavaScript.
2. Familiarity with a front-end framework (React, Angular, Vue).
3. Knowledge of backend concepts (Node.js, Python/Django, Ruby on Rails) if full-stack.
4. Be prepared for responsive design and cross-browser compatibility questions.
5. Showcase your portfolio projects effectively."""
    }
    return tips.get(role.lower(), f"General interview tips: Research the company, understand the job description, prepare STAR method answers for behavioral questions, and practice explaining your projects clearly.")

@tool
def suggest_project_ideas(domain: str) -> str:
    """Suggests project ideas for a specific career domain to build a portfolio.
    Input: The career domain (e.g., 'Machine Learning', 'Frontend Development').
    Output: A string with 3-5 project ideas.
    """
    st.info(f"Executing tool: suggest_project_ideas for domain: {domain}")
    ideas = {
        "data science": """Project Ideas for Data Science:
1. Build a sentiment analysis model for movie reviews.
2. Create a customer churn prediction model for a telecom company.
3. Analyze a public dataset (e.g., Kaggle) and create compelling visualizations.
4. Develop a recommendation system (e.g., for products or movies).""",
        "web development": """Project Ideas for Web Development:
1. Build a personal portfolio website.
2. Create a to-do list application with local storage.
3. Develop a simple e-commerce product listing page.
4. Recreate a famous website's landing page using modern frameworks.""",
        "ai engineering": """Project Ideas for AI Engineering:
1. Deploy a pre-trained ML model as a web service (e.g., with Flask/FastAPI).
2. Build an automated data pipeline for an ML workflow.
3. Create a custom chatbot using a fine-tuned LLM.
4. Implement a simple computer vision application (e.g., object detection)."""
    }
    return ideas.get(domain.lower(), f"No specific project ideas for {domain}. Think about real-world problems you can solve using skills in that domain!")


# List of all available tools
tools = [recommend_resources, generate_roadmap, career_outlook, interview_tips, suggest_project_ideas]

# --- LangGraph State Definition ---
# This defines the state that will be passed between nodes in the graph.
# Changed to TypedDict for LangGraph state management
class AgentState(TypedDict):
    # messages will be appended to using add_messages
    messages: Annotated[List[BaseMessage], add_messages]
    # intermediate_steps for UI display (dictionaries)
    intermediate_steps: List[Dict[str, Any]]

# --- LangGraph Nodes ---

# Node for the LLM agent to decide on its next action (Thought/Action)
def call_model(state: AgentState) -> Dict[str, Any]: # Node now returns a dictionary
    """
    Invokes the LLM to decide the next action (tool use or final answer).
    Updates the state with the LLM's thought and potential action.
    """
    st.markdown("--- **Agent Thinking** ---")
    st.markdown("🤖 Calling LLM for Thought/Action...")
    
    # Check if API key is set BEFORE initializing ChatGroq
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY environment variable not set. Please set it in your .env file.")
        raise ValueError("GROQ_API_KEY environment variable not set.")
        
    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key) # Pass api_key directly

    # Define the prompt for the ReAct agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful and comprehensive career mentor agent. Your goal is to assist users with career advice, learning resources, roadmaps, job outlooks, interview tips, and project ideas.
         You have access to the following tools:
         {tools}
         
         - Use 'recommend_resources' when the user asks for learning materials or resources for a specific domain.
         - Use 'generate_roadmap' when the user asks for a career roadmap for a specific domain.
         - Use 'career_outlook' when the user asks about job market trends, demand, or salary for a domain.
         - Use 'interview_tips' when the user asks for advice on preparing for interviews for a specific role.
         - Use 'suggest_project_ideas' when the user asks for project ideas to build a portfolio in a specific domain.
         
         If you need to use a tool, output a tool call.
         If you have enough information to answer the user's query, provide the final answer directly.
         Do NOT include "Thought:", "Action:", "Tool:", "Tool_Input:", "Answer:" in your final response content.
         Just provide the answer or the tool call.
         """),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]).partial(tools="\n".join([f"{t.name}: {t.description}" for t in tools]))

    # Bind tools to the LLM for function calling
    llm_with_tools = llm.bind_tools(tools)

    agent_runnable = prompt | llm_with_tools

    # --- Construct agent_scratchpad for the LLM from messages ---
    # The agent_scratchpad should contain previous AIMessage (with tool_calls) and ToolMessage
    llm_scratchpad = []
    # Iterate through the full history to build the scratchpad
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            llm_scratchpad.append(msg)
        elif isinstance(msg, ToolMessage):
            llm_scratchpad.append(msg)

    # Invoke the agent with the current messages and the correctly formatted scratchpad
    response = agent_runnable.invoke({
        "messages": state["messages"], 
        "agent_scratchpad": llm_scratchpad # Pass the correctly formatted scratchpad
    })

    # Prepare updates for the state
    new_intermediate_steps = list(state["intermediate_steps"]) # Create a mutable copy
    
    thought_text = ""
    action_type = "final_answer"
    tool_name = None
    tool_input = None

    if response.tool_calls:
        action_type = "tool_code"
        tool_call = response.tool_calls[0]
        tool_name = tool_call['name']
        tool_input = tool_call['args']
        # Infer thought based on tool call
        thought_text = f"I need to use the '{tool_name}' tool to get more information." 
    else:
        # Infer thought when providing a final answer
        thought_text = "I have enough information to provide a final answer."

    new_intermediate_steps.append({
        "type": "thought_action",
        "thought": thought_text,
        "action": action_type,
        "tool_name": tool_name,
        "tool_input": tool_input
    })

    # Return a dictionary to update the state
    return {"messages": [response], "intermediate_steps": new_intermediate_steps}

# Node for executing tools
def execute_tools(state: AgentState) -> Dict[str, Any]: # Node now returns a dictionary
    """
    Executes the tool called by the LLM.
    Updates the state with the tool's observation.
    """
    st.markdown("--- **Tool Execution** ---")
    st.markdown("🛠️ Executing Tools...")
    last_message = state["messages"][-1] # Access messages from the dictionary state
    tool_outputs = []
    new_intermediate_steps = list(state["intermediate_steps"]) # Create a mutable copy

    # Create a dictionary mapping tool names to tool functions for easy lookup
    tool_map = {tool.name: tool for tool in tools}

    for tool_call in last_message.tool_calls:
        tool_name = tool_call['name']
        tool_args = tool_call['args']
        
        if tool_name in tool_map:
            selected_tool = tool_map[tool_name]
            try:
                # Directly invoke the tool function with its arguments
                output = selected_tool.invoke(tool_args)
                # Ensure ToolMessage is created with the correct tool_call_id
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

    # Return a dictionary to update the state
    return {"messages": tool_outputs, "intermediate_steps": new_intermediate_steps}

# --- LangGraph Graph Definition ---

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("call_model", call_model)
workflow.add_node("execute_tools", execute_tools)

# Set the entry point
workflow.set_entry_point("call_model")

# Define conditional edges
workflow.add_conditional_edges(
    "call_model",
    lambda state: "execute_tools" if state["messages"][-1].tool_calls else END, # Access messages from state dict
    {
        "execute_tools": "execute_tools",
        END: END
    }
)

workflow.add_edge("execute_tools", "call_model")

# Compile the graph
app_graph = workflow.compile()

# --- Streamlit UI ---

st.set_page_config(page_title="Career Mentor ReAct Agent", layout="centered")

st.title("🎓 Career Mentor ReAct Agent")
st.markdown("Ask me anything about career advice, learning resources, or roadmaps!")
st.markdown("""
**Available functionalities:**
- **Learning Resources:** "Recommend resources for [domain]" (e.g., Data Science, Web Development)
- **Career Roadmaps:** "Generate a roadmap for [domain]" (e.g., AI Engineering, Cybersecurity)
- **Job Outlook:** "What is the career outlook for [domain]?" (e.g., Software Engineering, Marketing)
- **Interview Tips:** "Give me interview tips for a [role] role." (e.g., Data Scientist, Software Engineer)
- **Project Ideas:** "Suggest project ideas for [domain]." (e.g., Machine Learning, Frontend Development)
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
    # Add user message to session state messages (which is just a list)
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    with st.spinner("Agent is thinking..."):
        try:
            # Reset intermediate steps for each new query
            st.session_state.intermediate_steps = []
            
            # Create an initial state for the graph invocation
            # Pass the current messages from session_state to the graph
            initial_graph_state = {
                "messages": [HumanMessage(content=user_input)],
                "intermediate_steps": []
            }

            # Invoke the graph and get the final state
            final_graph_state = app_graph.invoke(initial_graph_state)

            # Update the session state with the final messages and intermediate steps
            # LangGraph's invoke returns the final state, where messages are accumulated.
            # We need to extract only the new messages generated by the agent.
            
            # Append new messages from the graph run to the session state
            # This approach relies on `add_messages` handling accumulation correctly.
            # We'll just append the last AI message or a summary of the tool output.
            # The intermediate steps already show the full process.
            
            # To avoid duplicating the user message and only add agent's responses:
            # Find the index of the user's initial message in the final_graph_state["messages"]
            # and add messages from that point onwards.
            user_msg_index = -1
            for i, msg in enumerate(final_graph_state["messages"]):
                if isinstance(msg, HumanMessage) and msg.content == user_input:
                    user_msg_index = i
                    break
            
            if user_msg_index != -1:
                new_agent_messages_from_graph = final_graph_state["messages"][user_msg_index+1:]
            else:
                new_agent_messages_from_graph = final_graph_state["messages"] # Fallback, might include user msg again

            # Filter out ToolMessages from direct chat display if they are already shown via intermediate_steps
            # and only add AIMessages for the main chat flow.
            for msg in new_agent_messages_from_graph:
                if isinstance(msg, AIMessage):
                    st.session_state.messages.append(msg)
                elif isinstance(msg, ToolMessage):
                    # Tool output is already displayed via st.info or st.error in execute_tools
                    # and captured in intermediate_steps. No need to add to main chat history here.
                    pass 

            st.session_state.intermediate_steps.extend(final_graph_state["intermediate_steps"])

            # Display the final answer from the agent (which should be the content of the last AIMessage)
            # This ensures the final answer is always displayed clearly.
            final_answer_to_display = "I couldn't generate a final answer. Please try again."
            for msg in reversed(st.session_state.messages): # Check session state messages for the last AI message
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
