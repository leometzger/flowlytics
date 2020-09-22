from ipaddress import IPv4Address
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from flowlytics.database import SQLBase


class DBIpSet(SQLBase):
    __tablename__ = "ipsets"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    ips = Column("ips", String)


# pydantic
class IpSet(BaseModel):
    id: Optional[int]
    name: str
    ips: List[str]

    @property
    def some_duplicated(self):
        return len(set(self.ips)) != len(self.ips)


    class Config:
        orm_mode = True


class CreateIpsetRequest(BaseModel):
    name: str
    ips: List[str]


class UpdateIpsetRequest(BaseModel):
    id: int
    name: str
    ips: List[str]
