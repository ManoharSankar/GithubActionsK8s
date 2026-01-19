from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="Production Python Microservice")

@app.get("/")
def root():
    return {"message": "Hello from Kubernetes microservice"}

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/config")
def config():
    return {"service_name": settings.SERVICE_NAME}
