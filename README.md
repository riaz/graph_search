### LLM Graph Search
This example is to enable ingesting and querying of any type of graph into neo4j or neptune
and perform natural language query on them, ideally we want everything to be in natural language
and for future versioin we want to be able to support multi-modal and multli-language

We also expose a api endpoint hosted on vercel.

CI/CD using github actions


Note: Vercel doesn't read pyproject.toml and needs requirment.txt, so we are using a library called - toml-to-requirements.
     pip install toml-to-requirements