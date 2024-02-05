import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
prompt = ChatPromptTemplate.from_template("Is this bms-llm?")

model = ChatOpenAI(
    base_url="https://typically-nearby-puma.ngrok-free.app/v1", 
    api_key="not-needed",
    streaming=True,
    temperature=0.2,
)
chain = prompt | model

response = chain.invoke({})
for chunk in response:
    print(chunk[1])