import google.generativeai as genai

genai.configure(api_key="AIzaSyBQEKjsPCkt8qxizWHMe1EtZTBsgBqifyI")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Resuma o livro pai rico e pai pobre em json, 5 topicos")
print(response.text)