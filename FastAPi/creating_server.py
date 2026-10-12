from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to Home Page."


@app.get("/main")
def main():
    return "This is main page"