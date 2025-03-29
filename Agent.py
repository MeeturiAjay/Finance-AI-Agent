from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["PHIDATA_API_KEY"] = os.getenv("PHIDATA_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search web for Information.",
    tools = [DuckDuckGo()],
    model = Groq(id = "llama-3.3-70b-versatile"),
    instructions = ["Always include sources"],
    show_tool_calls = True,
)

# Finance Agent
finance_agent = Agent(
    name = "Finance Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    instructions = ["Use tables to display the data"],
    show_tool_calls = True
)

multi_agent = Agent(
    team = [web_search_agent, finance_agent],
    instructions = ["Always include sources", "Use tables to display the data"],
    show_tool_calls = True,
)

multi_agent.print_response("What is the difference between the NVIDIA & Tesla's share prices? Which one should I buy?")