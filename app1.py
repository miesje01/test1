from flask import Flask
from openai import AzureOpenAI
import os

app = Flask(__name__)

client = AzureOpenAI(
    api_key= os.environ["OPENAI_API_KEY"],
    azure_endpoint=os.environ["OPENAI_ENDPOINT"],
    api_version="2025-04-01-preview"
)

@app.route("/")
def root():
    response = client.responses.create(
        model="gpt-5.5",
        input="Hu lang is een chinees?"
    )
    return response.output_text

@app.route("/ask/<vraag>")
def ask(vraag):
    response = client.responses.create(
        model="gpt-5.5",
        input=vraag
    )
    return response.output_text

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8080)
