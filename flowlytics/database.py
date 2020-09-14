import sqlalchemy
import databases

from fastapi import FastAPI


DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

db_ipsets = sqlalchemy.Table(
    "ipsets",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("ips", sqlalchemy.String),
)

db_queries = sqlalchemy.Table(
    "queries",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
