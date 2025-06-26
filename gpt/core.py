from openai import OpenAI
from dotenv import load_dotenv
from gpt_context import context as cont
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("gpt_key"))

class gptHandler:
    def llm_call(system, user):
        # Dynamically import the sub class from GPTContext using the theme parameter
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[  
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ]  
        )
        
        return completion.choices[0].message.content.strip()