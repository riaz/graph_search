from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .database import GraphDatabase
from .nl_to_cypher import nl_to_cypher

app = FastAPI()
db =  GraphDatabase()

class Query(BaseModel):
    natural_language: str

@app.get("/")
async def root():
    return {"message": "Hello World"}    

@app.post("/execute/")
async def execute_query(query: Query):
    try:
        cypher_query = nl_to_cypher(query.natural_language)
        result = db.execute_query(cypher_query)
        return {"cypher_query": cypher_query, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health/")
async def health_check():
    return {"status": "healthy"}

@app.lifespan("shutdown")
def shutdown_event():
    db.close()