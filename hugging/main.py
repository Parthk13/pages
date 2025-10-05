from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

TOKEN = os.environ.get("GA2-2E2F9B", None)


@app.get("/")
def read_root():
    port = os.getenv("APP_PORT", "N/A")
    return {"message": f"Hello from Hugging Face Docker Space on port {port}!"}


@app.get("/token")
def token():
    if TOKEN:
        return {"success": True, "token": TOKEN[:4]}
    else:
        raise HTTPException(status_code=404, detail="Token not found")
