from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    return {"data": "vikash"}

@app.get("/blog")
def blog():
    return {"data": "blog page"}  

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}   

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}   


@app.get("/blog/{id}/comment")
def show(id):
    return {"data": {"1","2"}}         