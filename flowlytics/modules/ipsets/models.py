from typing import List, Optional
from ipaddress import IPv4Address
from pydantic import BaseModel


class IpSet(BaseModel):
    id: Optional[str]
    name: str
    ips: List[str]

    def __init__(self, id, name, ips=[]):
        self.id = id
        self.name = name
        self.ips = ips

    @property
    def some_duplicated(self):
        return len(set(self.ips)) != len(self.ips)


class CreateIpsetRequest(BaseModel):
    name: str
    ips: List[str]


class UpdateIpsetRequest(BaseModel):
    id: int
    name: str
    ips: List[str]
