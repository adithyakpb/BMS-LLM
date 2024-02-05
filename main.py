import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(base_url="http://localhost:80/v1", api_key="not-needed")

user_query = ""
while user_query != "exit":
    user_query = ""
    user_query = input("\nEnter your query:")
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI assistant for an engineering college in Bengaluru, Karnataka, India. The name of the college is B.M.S College of Engineering. Your name is 'BMS-Bot'."},
        {"role": "assistant", "content" : "Please answer all questions ethically, honestly and responsibly. If you do not know the answer to a question, please say so."},
        {"role": "user", "content": f"{user_query}"},
    ],
    stream=True,
    temperature=0.2
    )
    for chunk in response:
        print(chunk.choices[0].delta.content, end='', flush=True)
    
