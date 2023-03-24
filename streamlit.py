import openai
import streamlit as st
import os
# pip install streamlit-chat
from streamlit_chat import message

openai.api_key=os.getenv("MY_CHATGPT_API")

chat_history = [{"role": "system", "content": "You are a helpful AI assistant."}]

# def generate_response(prompt):
#     # completions = openai.Completion.create(
#     #     engine = "text-davinci-003",
#     #     prompt = prompt,
#     #     max_tokens = 1024,
#     #     n = 1,
#     #     stop = None,
#     #     temperature=0.5,
#     # )
#     chat_history += [{"role": "user", "content": prompt}]
#     completions = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=chat_history
#         )
#     message = completions.choices[0].text
#     return message


# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text


#Creating the chatbot interface
st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


user_input = get_text()

if user_input:
    #output = generate_response(user_input)
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            chat_history += [{"role": "user", "content": st.session_state['past'][i]}]
            chat_history += [{"role": "assistant", "content": st.session_state["generated"][i]}]

    chat_history += [{"role": "user", "content": user_input}]
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
        )
    output = completions['choices'][0]['message']['content']
    chat_history += [{"role": "assistant", "content": output}]

    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
