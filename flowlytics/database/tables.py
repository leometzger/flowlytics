from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from flowlytics.database import SQLBase


class DBIpSet(SQLBase):
    __tablename__ = "ipsets"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    ips = Column("ips", String)


class DBFilter(SQLBase):
    __tablename__ = "filters"

    id = Column("id", Integer, primary_key=True)
    start_date = Column("start_date", Date)
    end_date = Column("end_date", Date)
    port = Column("port", Integer)
    protocol = Column("protocol", String)
    query = relationship("DBQuery", back_populates="filters")


class DBQuery(SQLBase):
    __tablename__ = "queries"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    filters_id = Column(Integer, ForeignKey('filters.id'))
    filters = relationship("DBFilter",  uselist=False, back_populates="query")
