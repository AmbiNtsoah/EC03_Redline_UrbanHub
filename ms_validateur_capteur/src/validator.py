from fastapi import FastAPI
from src.endpoints.routes import router

app = FastAPI(title="Portal Validator Service")

app.include_router(router)