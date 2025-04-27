from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserConfig, Browser
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

from lmnr import Laminar
# this line auto-instruments Browser Use and any browser you use (local or remote)
Laminar.initialize(project_api_key=os.getenv("LMNR_PROJECT_API_KEY"))

config = BrowserConfig(
    headless=True
)

browser = Browser(config=config)

async def main():
    agent = Agent(
        browser=browser,
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())