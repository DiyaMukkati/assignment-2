import requests
import os

API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def query_huggingface(prompt):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return response.json()
    except Exception as e:
        return "Error: " + str(e)


prompt = input("Enter your prompt: ")

print("Querying HuggingFace...")

result = query_huggingface(prompt)

print("Response:")
print(result)