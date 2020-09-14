from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

SQLBase = declarative_base()


class IpSet(SQLBase):
    __tablename__ = "ipsets"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    ips = Column("ips", String)


class Query(SQLBase):
    __tablename__ = "queries"

    id = Column("id", Integer, primary_key=True),
    name = Column("name", String),
