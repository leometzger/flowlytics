from ipaddress import IPv4Address
from pydantic import BaseModel
from typing import List, Optional


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

