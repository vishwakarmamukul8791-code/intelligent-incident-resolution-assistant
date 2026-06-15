import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
print(os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

for m in genai.list_models():
    print(m.name)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def generate_answer(
    question,
    context
):

    prompt = f"""
    Answer the question using only the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(
        prompt
    )

    return response.text