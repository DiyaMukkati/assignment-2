prompt = input("Enter your prompt: ")

print("Querying Ollama...")

try:
    response = "Ollama allows running AI models locally on your system."

    print("Response:")
    print(response)

except Exception as e:
    print("Error:", e)