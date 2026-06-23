from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key= os.environ["OPENAI_API_KEY"],
    azure_endpoint=os.environ["OPENAI_ENDPOINT"],
    api_version="2025-04-01-preview"
)

response = client.responses.create(
    model="gpt-5.5",
    input="Hu lang is een chinees?"
)
print(response.output_text)
