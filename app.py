import os
from dotenv import load_dotenv
from models.nvidia_llm import llm
from Prompts.system_prompt import SYSTEM_PROMPT
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    ToolMessage,
)
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

import Rag.LangGraph_agent


agent = Rag.LangGraph_agent.get_agent()

messages = []

print("=" * 50)
print("🤖 Tax Planning AI Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        print("\nGoodbye 👋")
        break

    messages.append(
        HumanMessage(content=question)
    )

    response = agent.invoke(
        {
            "messages": messages
        }
    )

    messages = response["messages"]

    print("\nAI :", messages[-1].content)