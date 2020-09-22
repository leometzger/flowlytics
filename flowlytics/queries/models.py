from ipaddress import IPv4Address
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from flowlytics.database import SQLBase


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


# pydantic
class Filters(BaseModel):
  start_date: Optional[str]
  end_date: Optional[str]
  port: Optional[int]
  protocol: Optional[str]
  source_ip: Optional[str]
  destination_ip: Optional[str]

  class Config:
    orm_mode = True


class RunQuery(BaseModel):
  sensor: str
  ipset: str


class Query(BaseModel):
  id: Optional[int]
  name: str
  filters: Filters

  class Config:
    orm_mode = True


class CreateQueryRequest(Query):
  pass


class UpdateQueryRequest(Query):
  pass

