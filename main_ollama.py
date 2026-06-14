from langchain.chat_models import init_chat_model


model = init_chat_model(
    model='llama3.2:1b',
    model_provider="ollama" #this running on our laptop  by 'ollama pull llama3.2:1b' in terminal
)

response = model.invoke("Can I learn Python in one year?")
print(response.text)