from ipaddress import IPv4Address
from pydantic import BaseModel
from typing import List, Optional


class Filters(BaseModel):
    start_date: str
    end_date: str
    port: int
    protocol: str
    source_ip: str
    destination_ip: str


class RunQuery(BaseModel):
  sensor: str
  ipset: str


class Query(BaseModel):
  id: Optional[str]
  name: str
  filters: Filters


class CreateQueryRequest(Query):
  pass


class UpdateQueryRequest(Query):
  pass

