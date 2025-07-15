from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def hello():
    return {"data": "Hello"}

@app.get("/echo")
def echo(text: str = Query(..., description="Text to echo back")):
    return {"echo": text+" thank you using this api!!"}
