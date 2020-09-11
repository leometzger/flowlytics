import flowlytics.config as config

from fastapi import FastAPI
from flowlytics.api import router


api = FastAPI()
api.include_router(router, prefix="/api")
