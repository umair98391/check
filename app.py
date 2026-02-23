from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}
