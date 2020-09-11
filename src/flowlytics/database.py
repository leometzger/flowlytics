import sqlalchemy
import databases

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

BaseModel = declarative_base()
