from fastapi import FastAPI
from .api import router
from flowlytics.database import SQLBase, engine

SQLBase.metadata.create_all(engine)

api = FastAPI()
api.include_router(router, prefix="/api")
