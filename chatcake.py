import openai
import os

print("\033[92m" + " ______     __  __     ______     ______   ______     ______     __  __     ______    " + "\033[0m")
print("\033[92m" + "/\  ___\   /\ \_\ \   /\  __ \   /\__  _\ /\  ___\   /\  __ \   /\ \/ /    /\  ___\   " + "\033[0m")
print("\033[92m" + "\ \ \____  \ \  __ \  \ \  __ \  \/_/\ \/ \ \ \____  \ \  __ \  \ \  _\"-.  \ \  __\   " + "\033[0m")
print("\033[92m" + " \ \_____\  \ \_\ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\\ " + "\033[0m")
print("\033[92m" + "  \/_/____/  \/_/\/_/   \/_/\/_/     \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/ " + "\033[0m")
print("\033[91m" + "                                  Created by t4ps3c"+ "\033[0m")
print("")

openai.api_key = os.getenv=("OPENAI_API_KEY")

while True:
    user_msg = input("\033[94m" +"You: "+"\033[0m")
    if user_msg.lower() in ["exit", "quit"]:
        break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
  	messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
  	{"role": "user", "content" : "How are you?"},
  	{"role": "assistant", "content" : "I am doing well"},
  	{"role": "user", "content" : user_msg }]
        )

    print("\033[38;5;208m" +"ChatCake: "+"\033[0m" + completion["choices"][0]["message"]["content"])
    print("")
  
