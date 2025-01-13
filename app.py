import os
import streamlit as st
from crewai import Agent, Task, Crew
from crewai.llm import LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import chromadb
#from googletrans import Translator

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AI News Generator", page_icon="📰", layout="wide")

# Translator for multilingual support
#translator = Translator()

# Title and description
st.title("🤖 AI News Generator Bot 📰")
st.markdown("This AI Bot generates blog posts about any topic you ask it.")

# Sidebar
with st.sidebar:
    st.header("Content Settings")
    
    # Make the text input take up more space
    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="Enter the topic you want to generate content about..."
    )

    # Validate Input
    if not topic.strip():
        st.warning("Please enter a valid topic to proceed.")
        st.stop()
    
    # Language Selection
    #language = st.selectbox("Choose output language", ["English", "Spanish", "French", "German", "Chinese"])
    #language_mapping = {"English": "en", "Spanish": "es", "French": "fr", "German": "de", "Chinese": "zh-cn"}

    
    # sidebar controls
    st.markdown("### Advanced Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Add some spacing
    st.markdown("---")
    
    # Make the generate button more prominent in the sidebar
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)
    
    # Helpful information
    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Enter your desired topic in the text area above
        2. Adjust the temperature if needed (higher = more creative)
        3. Click 'Generate Content' to start
        4. Wait for the AI to generate your article
        5. Download the result as a markdown file
        """)

def generate_content(topic):
    llm = LLM(
        model="command-r",
        temperature=0.7
    )

    search_tool = SerperDevTool(n_results=10)

    # First Agent: Senior News Correspondent
    senior_research_analyst = Agent(
        role="Senior News Correspondent",
        goal=f"Research and conduct thorough journalistic research and create an organized news report on this {topic} from reliable web sources",
        backstory="You are a Senior News Correspondent known for delivering accurate, insightful, and balanced news reports. "
                "You specialize in identifying key trends, providing a historical context, and crafting concise yet impactful summaries "
                "Your task is to investigate the topic thoroughly by sourcing reliable information, and analyzing current events, "
                " and fact-checking all details."
                "Your output should include a structured and well-researched news report that highlights the core of the topic,"
                "includes citations, and adheres to journalistic standards of neutrality and clarity.",
        allow_delegation=False,
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # Second Agent: Technical Content Writer
    technical_writer = Agent(
        role="Content Writer",
        goal="Transform research and news reports into engaging, audience-friendly blog posts with clear technical explanations while maintaining accuracy",
        backstory="You are a Technical Copywriter skilled at converting detailed reports into accessible,"
                "engaging content tailored to various audiences. "
                "You work closely with the Senior News Correspondent and excel at maintaining the perfect "
                "balance between informative and entertaining writing, "
                "while ensuring all facts and citations from the research "
                "are properly incorporated. Your writing should feature an engaging introduction, a logically structured body, and a compelling conclusion"
                "You have a talent for making complex topics approachable without oversimplifying them.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # Research Task
    research_task = Task(
        description=("""
            1. Conduct comprehensive research on {topic} including:
                - Recent developments and news
                - Key industry trends and innovations
                - Expert opinions and analyses
                - Statistical data and market insights
            2. Evaluate source credibility and fact-check all information
            3. Organize findings into a structured research brief
            4. Include all relevant citations and sources
        """),
        expected_output="""A detailed research report containing:
            - Executive summary of key findings
            - Comprehensive analysis of current trends and developments
            - List of verified facts and statistics
            - All citations and links to original sources
            - Clear categorization of main themes and patterns
            Please format with clear sections and bullet points for easy reference.""",
        agent=senior_research_analyst
    )

    # Writing Task
    writing_task = Task(
        description=("""
            Using the research brief provided, create an engaging blog post that:
            1. Transforms technical information into accessible content
            2. Maintains all factual accuracy and citations from the research
            3. Includes:
                - Attention-grabbing introduction
                - Well-structured body sections with clear headings
                - Compelling conclusion
            4. Preserves all source citations in [Source: URL] format
            5. Includes a References section at the end
        """),
        expected_output="""A polished blog post in markdown format that:
            - Engages readers while maintaining accuracy
            - Contains properly structured sections
            - Includes Inline citations hyperlinked to the original source url
            - Presents information in an accessible yet informative way
            - Follows proper markdown formatting, use H1 for the title and H3 for the sub-sections""",
        agent=technical_writer
    )

    # Create Crew
    crew = Crew(
        agents=[senior_research_analyst, technical_writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic})

# Main content area
if generate_button:
    with st.spinner('Generating content... This may take a moment.'):
        try:
            result = generate_content(topic)
            st.markdown("### Generated Content")
            st.markdown(result)
            
            # Add download button
            st.download_button(
                label="Download Content",
                data=result.raw,
                file_name=f"{topic.lower().replace(' ', '_')}_article.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
