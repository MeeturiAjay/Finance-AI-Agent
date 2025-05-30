from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["PHIDATA_API_KEY"] = os.getenv("PHIDATA_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search web for information.",
    tools=[DuckDuckGo()],
    model=Groq(id="llama-3.3-70b-specdec"),
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    return_task_output=True
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-specdec"),
    tools=[YFinanceTools()],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    return_task_output=True  # Forces it to return a response
)

# Multi-Agent System
multi_agent = Agent(
    name="Multi-Agent System",
    role="Combine responses from web search and finance.",
    tools=[DuckDuckGo(), YFinanceTools()],
    model=Groq(id="llama-3.3-70b-specdec"),
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    return_task_output=True
)

# Ask Question
multi_agent.print_response("Now tell me how should a beginner start with which stocks? which company?")
