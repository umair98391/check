from fastapi import FastAPI
import uvicorn

# Create FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello Umair, How are You!"}


# This makes the file executable directly
if __name__ == "__main__":
    uvicorn.run(
        "main:app",      # filename:app_variable
        host="0.0.0.0",  # accessible from network
        port=8000
    )
