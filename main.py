from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

@app.get("/")
def index():
    return {"data": "vikash"}

@app.get("/blog")
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blog from the db"}
    else:
         return {"data": f"{limit} blog from the db"}  

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}   

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}   


@app.get("/blog/{id}/comment")
def comment(id, limit=10):
    return {"data": {"1","2"}}  

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]   

@app.post("/blogs")
def create_blog(blog: Blog):
    
    return {"data": f"Blog is created with title as {blog.title}"}          