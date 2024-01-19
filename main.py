from typing import Union
from utils.script import Search
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search/{query}")
def Search_query(query: str = None):
    if query is None:
        raise HTTPException(status_code=400, detail="Query is required")
    search_data = Search(query)
    return {"results": search_data}