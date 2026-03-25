import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyCHR3LJDMD6pyL7_ikEY7cCGA0dKDnk9Yk"))

model = genai.GenerativeModel("gemini-1.5-flash")

def query_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Error: " + str(e)


prompt = input("Enter your prompt: ")

print("Querying Gemini...")

result = query_gemini(prompt)

print("Response:")
print(result)