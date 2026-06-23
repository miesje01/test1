from openai import AzureOpenAI
client = AzureOpenAI(
    api_key= "4VO….j",
    azure_endpoint="https://aro-openai.cognitiveservices.azure.com/openai/responses?",
    api_version="2025-04-01-preview"
)
#print("Connected")\
response = client.responses.create(
    model="gpt-5.5",
    input="Hallo"
)
print(response.output_text)
