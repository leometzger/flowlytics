import databases

from sqlalchemy import create_engine, Table
from .tables import SQLBase, Query as DBQuery, IpSet as DBIpset

DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SQLBase.metadata.create_all(engine)


class FlowlyticsDb():
    def __init__(self, queries: DBQuery, ipsets: DBIpset):
        self.queries = queries
        self.ipsets = ipsets


flowlytics_db = FlowlyticsDb(
    queries=DBQuery,
    ipsets=DBIpSet
)


def get_db() -> FlowlyticsDb:
    return flowlytics_db
