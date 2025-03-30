from phi.tools.yfinance import YFinanceTools
import phi.api
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import phi
from phi.playground import Playground, serve_playground_app
from phi.model.groq import Groq

load_dotenv()

phi.api = os.getenv("PHIDATA_API_KEY")

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

app = Playground(agents = [web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("code_ground:app", reload = True)