import openai
import os
openai.api_key=os.getenv("MY_CHATGPT_API")

# turn on proxy before you run this api

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
print("Welcome to ChatGPT, turn on proxy before you run this api")

while True:
    user_input = input("Q: ")
    if user_input.lower() == "exit":
        break
    
    chat_history += [{"role": "user", "content": user_input}]
    chatgpt_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
        )
    
    print(chatgpt_resp['choices'][0]['message']['content'])
    chat_history += [{"role": "assistant", "content": chatgpt_resp['choices'][0]['message']['content']}]


with open("chat_history.txt", "a") as file:
    for message in chat_history:
        file.write(f"{message['content']}\n")