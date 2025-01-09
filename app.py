import os
import streamlit as st
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title=" AI News Generator 📰", page_icon="📰", layout="wide")

# Title and description
st.title("🤖 AI News Generator Bot")
st.markdown("This bot produces blog posts about any topic you request for.")

# Sidebar
with st.sidebar:
    st.header("Content Settings")
    
    # Topic Input
    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="Enter the topic you want to generate content about..."
    )

    # Validate Input
    if not topic.strip():
        st.warning("Please enter a valid topic to proceed.")
        st.stop()

   # Add more sidebar controls if needed
    st.markdown("### Advanced Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Add some spacing
    st.markdown("---")
    
    # Generate Button
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)

def generate_content(topic, temperature):
    llm = LLM(
        model="command-r",
        temperature=temperature
    )

senior_research_analyst = Agent(
        role="Senior Research Analyst",
        goal=f"Research, analyze, and synthesize comprehensive information on {topic}",
        backstory="You're an expert research analyst with advanced web research skills. "
                "You excel at finding, analyzing, and synthesizing information from "
                "across the internet using search tools. You're skilled at "
                "distinguishing reliable sources from unreliable ones, "
                "fact-checking, cross-referencing information, and "
                "identifying key patterns and insights. You provide "
                "well-organized research briefs with proper citations "
                "and source verification. Your analysis includes both "
                "raw data and interpreted insights, making complex "
                "information accessible and actionable.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )
