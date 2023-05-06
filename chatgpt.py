import openai
import os

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
openai.api_key = os.environ["OPENAI_API_KEY"]

while True:
    user_msg = input("You: ")
    if user_msg.lower() in ["exit", "quit"]:
        break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
  	messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
  	{"role": "user", "content" : "How are you?"},
  	{"role": "assistant", "content" : "I am doing well"},
  	{"role": "user", "content" : user_msg }]
        )

    print("chatgpt: " + completion["choices"][0]["message"]["content"])
    print("")
    print("")
