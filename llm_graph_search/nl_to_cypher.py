import os
from dotenv import dotenv_values
import openai

#secrets = dotenv_values('.env.test')
#API_KEY = secrets["LLM_API_KEY"]

def nl_to_cypher(query):
    client = openai.OpenAI(
        base_url = "https://api.endpoints.anyscale.com/v1",
        # Replace with long-lived credentials for production
        api_key = os.environ.get("LLM_API_KEY")
    )

    # Note: not all arguments are currently supported and will be ignored by the backend.
    response = client.chat.completions.create(**{
    "model": "meta-llama/Meta-Llama-3-70B-Instruct",
    "messages": [
        {"role": "system", "content": "Translate the following natural language query to a Cypher query"},
        {"role": "user", "content": query},
        {"role": "assistant", "content": "Cypher Query:"}
    ],
    "temperature": 1,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0
    })    
    
    return response.choices[0].message.content
    