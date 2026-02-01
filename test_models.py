from google import genai

client = genai.Client(api_key="AIzaSyDafusF51t5PQsupFlckdtJfDideSXVWnE")

models = client.models.list()

for model in models:
    print(model.name)
