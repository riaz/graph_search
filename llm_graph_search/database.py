import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from gremlinpython.driver import client, serializer
from gremlinpython.driver.protocl import GremlinServerError


# Note: we will make use of a env file to fetch the server configuration we are looking for
load_dotenv()

class GraphDatabase():
    def __init__(self):
        self.db_type  = os.getenv("DB_TYPE", "neoe4j") # default being neo4j
        
        if self.db_type == "neo4j":
            uri = os.getenv("NEO4J_URI")
            user = os.getenv("NEO4J_USER")
            password = os.getenv("NEO4J_PASSWORD")
            self.driver = GraphDatabase.driver(uri, auth=(user, password))

        elif self.db_type == "neptune":
            endpoint = os.getenv("NEPTUNE_ENDPOINT")
            port = os.getenv("NEPTUNE_PORT")
            self.client = client.Client(f"wss://{endpoint}:{port}/gremlin", "g", 
                                        message_serializer=serializer.GraphSONSerializersV2d0())
        else:
            # an invalid db type was encountered
            raise ValueError("Invalid database type specified")
    
    def close(self):
        if self.db_type == "neo4j":
            self.driver.close()
        elif self.db_type == "neptune":
            self.client.close()

    def execute_query(self, query, params=None):
        if self.db_type == "neo4j":
            with self.driver.session() as session:
                result = session.run(query, params)
                return [record.data() for record in result]
        elif self.db_type == "neptune":
            result = self.client.submit(query, params)
            return [item.as_dict() for item in result]