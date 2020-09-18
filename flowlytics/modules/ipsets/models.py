from ipaddress import IPv4Address
from pydantic import BaseModel
from typing import List, Optional


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
