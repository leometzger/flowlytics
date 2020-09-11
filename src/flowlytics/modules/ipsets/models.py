from typing import List, Optional
from ipaddress import IPv4Address
from pydantic import BaseModel

from sqlalchemy import Table, Integer, String, Column

metadata = MetaData()
ipsets = Table(
    "ipsets",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("ips", String)
)

class IpSet(BaseModel):
  id: Optional[str]
  name: str
  ips: List[str]

  @property
  def some_duplicated(self):
    return len(set(self.ips)) != len(self.ips)


## Requests

class CreateIpsetRequest:
  name: str
  ips: List[str]


class UpdateIpsetRequest:
  id: int
  name: str
  ips: List[str]