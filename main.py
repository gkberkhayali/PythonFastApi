from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the application!"}

@app.get("/Test")
def welcomeTest():
    return {"message": "Test Get request successful!"}

@app.get("/Test/Test2")
def welcomeTest2():
    return {"message": "Test2 Get request successful!"}