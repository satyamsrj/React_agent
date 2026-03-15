from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import TavilySearchResults
from langchain.agents import create_react_agent

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define tools
search_tool = TavilySearchResults(search_depth="basic")
tools = [search_tool]

# Create agent (new API)
agent = create_react_agent(llm=llm, tools=tools, verbose=True)

# Run agent
result = agent.invoke({"input": "Give me a tweet about the weather in New York City today"})
print(result)