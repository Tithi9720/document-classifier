from fastapi import FastAPI
from app.classifier import classify_text 

app = FastAPI()

@app.post("/classigy")
def classfiy(document: dict):
    text = document["text"]

    return classify_text(text)