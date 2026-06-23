from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tavily import TavilyClient

tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """Search for information and return the result."""
    # Implement your search logic here
    print(f"Search results for '{query}'")
    return tavily.search(query=query)

llm =  ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-projects!")
    result = agent.invoke({"messages":[HumanMessage(content="What is the weather in Pune?")]})
    print(result)

if __name__ == "__main__":
    main()
