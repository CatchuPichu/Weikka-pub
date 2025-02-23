#Hakee OpenAI- ja Gradio ohjelman
import openai
import gradio

#OpenAI API avain
openai.api_key = "avaimesi"

#Kysyy käyttäjältä tämän promptin
messages = [{"role": "system", "content": "Ohjeet chattibotille tähän."}]

#Chattibotin vastaus
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"] [0] ["message"] ["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

#Gradio näkymä
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Weikka")

#Avaa Gradion
demo.launch()