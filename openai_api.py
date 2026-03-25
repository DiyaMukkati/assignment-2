from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("API not available, showing sample response.")
        return "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence."


prompt = input("Enter your prompt: ")

print("Querying OpenAI...")

result = query_openai(prompt)

print("Response:")
print(result)