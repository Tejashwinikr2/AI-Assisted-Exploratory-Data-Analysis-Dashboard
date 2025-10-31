import google.generativeai as genai
genai.configure(api_key="AIzaSyBYGhDg9Ugtr0w2Px4TRFhj5LLuWgJg7a0")

for m in genai.list_models():
    print(m.name)
