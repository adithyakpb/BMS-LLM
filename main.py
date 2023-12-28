import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

user_query = ""
while user_query != "exit":
    user_query = ""
    user_query = input("Enter your query:")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are BMS-Assistant, a chatbot that answers questions about BMS College of Engineering."},
        {"role": "assistant", "content" : "Please answer all questions ethically, honestly and responsibly. If you do not know the answer to a question, please say so."},
        {"role": "user", "content": f"{user_query}"},
    ]
    )
    print(completion.choices[0].message.content)
    
