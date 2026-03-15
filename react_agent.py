from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import TavilySearchResults
from langchain.agents import create_react_agent_executor
from langchain.agents import tool

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define tools
search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(foreccast: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Get the current system time in the specified format."""
    from datetime import datetime
    return datetime.now().strftime(foreccast)

tools = [search_tool, get_system_time]

# Create agent executor (new API)
agent = create_react_agent_executor(llm=llm, tools=tools, verbose=True)

# Run agent
result = agent.invoke({"input": "when was ISRO last launch and how many days ago was it?"})
print(result)