from fastapi import FastAPI
from .api import router

api = FastAPI()
api.include_router(router, prefix="/api")
