import os
import openai

api_key = os.getenv("LLM_API_KEY")

def nl_to_cypher(query):
    prompt = f"""
    Translate the following natural language query to a Cypher query
    {query}

    Cypher Query:
    """

    client = openai.OpenAI(
        base_url = "https://api.endpoints.anyscale.com/v1",
        # Replace with long-lived credentials for production
        api_key = api_key
    )

    # Note: not all arguments are currently supported and will be ignored by the backend.
    response = client.chat.completions.create(**{
    "model": "meta-llama/Meta-Llama-3-70B-Instruct",
    "messages": [prompt],
    "temperature": 1,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0
    })

    cypher_query = response.choice[0].text.strip()

    return cypher_query