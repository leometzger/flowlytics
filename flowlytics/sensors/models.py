from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from flowlytics.database import SQLBase


class DBNetworkGroup(SQLBase):
  __tablename__ = "network_groups"

  id = Column("id", Integer, primary_key=True)
  ip_blocks = Column("ip_blocks", String)
  sensor = relationship("DBSensor", back_populates="network_group")


class DBSensor(SQLBase):
  __tablename__ = "sensors"  

  id = Column("id", Integer, primary_key=True)
  description = Column("description", String)  
  listen_port = Column("listen_port", Integer)
  protocol = Column("protocol", String)
  listen_as_host = Column("listen_as_host", String)
  network_group_id = ForeignKey(Integer, "nework_group.id")
  network_group = relationship("DBNetworkGroup", uselist=False, back_populates="sensor")
 

# pydantic
class NetworkGroup(BaseModel):
  id: Optional[int]
  ip_blocks: List[str]


class Sensor(BaseModel):
  id: Optional[int]
  description: str
  listen_port: int
  protocol: str
  listen_as_host: str
  network_group: NetworkGroup


class Field(Enum):
   S_IP=1
   D_IP=2
   S_PORT=3
   D_PORT = 4
   PROTO = 5
   PACKETS = 6
   BYTES = 7
   FLAGS = 8
   S_TIME= 9
   DURATION = 10
   E_TIME = 11
   SENSOR = 12
   IN = 13
   OUT = 14
   NH_IP = 15
   S_TYPE = 16
   D_TYPE = 16
   SCC = 18
   DCC = 19
   CLASS = 20
   TYPE = 21
   ICMP_TYPE = 25
   INITIAL_FLAGS = 26
   SESSION_FLAGS = 27
   ATTRIBUTTES = 28
   APPLICATION = 29
