from google import genai

client = genai.Client(api_key="AIzaSyC_H8R0s6EVcavO5rG2_99DG7DFxWM33aA")

models = client.models.list()

for m in models:
    print(m.name)