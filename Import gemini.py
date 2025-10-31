import google.generativeai as genai
genai.configure("ADD_YOUR_GEMINI_API_KEY")
for m in genai.list_models():
  print(m.name)
