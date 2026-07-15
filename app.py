import os
from dotenv import load_dotenv
from models.nvidia_llm import llm

response = llm.invoke("What is HRA?")

print(response.content)
