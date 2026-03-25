import cohere
import os

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=100
        )
        return response.generations[0].text

    except Exception as e:
        return "Error: " + str(e)


prompt = input("Enter your prompt: ")

print("Querying Cohere...")

result = query_cohere(prompt)

print("Response:")
print(result)