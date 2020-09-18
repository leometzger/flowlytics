from sqlalchemy import Table, Column, Integer, String
from flowlytics.database import SQLBase


class DBIpSet(SQLBase):
    __tablename__ = "ipsets"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    ips = Column("ips", String)


class DBQuery(SQLBase):
    __tablename__ = "queries"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
