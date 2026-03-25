from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        )

        return chat.choices[0].message.content

    except Exception as e:
        print("API error, showing sample response.")
        return "Groq provides very fast AI inference for models like Llama."


prompt = input("Enter your prompt: ")

print("Querying Groq...")

result = query_groq(prompt)

print("Response:")
print(result)