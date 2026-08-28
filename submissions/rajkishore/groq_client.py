import os
from dotenv import load_dotenv

from groq import Groq

client = None

def ask_llm(prompt):
    global client

    if client is None:
        load_dotenv()
        api_key=os.environ.get("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is not set. Add it to your environment or .env file.")
        
        client = Groq(api_key=api_key)

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_completion_tokens=512,
        top_p=1,
        stream=True
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            yield content