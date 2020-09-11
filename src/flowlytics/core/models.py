from enum import Enum

class Flow:
  def __init__(self, source_ip, destination_ip, protocol, port, packets, flow_bytes):
    self.source_ip = source_ip
    self.destination_ip = destination_ip
    self.protocol = protocol
    self.port = port
    self.bytes = flow_bytes


class Counter:
  def __init__(self, field_type, value, packets, flow_bytes):
    self.field_type = field_type
    self.value = value
    self.packets = packets
    self.bytes = flow_bytes


class Filters:
  def __init__(self, 
    start_date=None, 
    end_date=None, 
    port=None, 
    protocol=None,
    source_ip=None, 
    destination_ip=None,
    sensor=None,
    input_file=None
  ):
    self.start_date = start_date
    self.end_date = end_date
    self.port = port
    self.protocol = protocol
    self.source_ip = source_ip
    self.destination_ip = destination_ip
    self.sensor = sensor
    self.input_file = input_file


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
