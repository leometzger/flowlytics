from sqlalchemy.orm import Session
from flowlytics.sensors.models import Sensor, DBSensor, DBNetworkGroup
from typing import List


def get_all(db: Session) -> List[DBSensor]:
    return db.query(DBNetworkGroup).all()


def find_by_id(db: Session, id: str) -> DBSensor:
    return db.query(DBNetworkGroup).filter(DBNetworkGroup.id == id).first()


def create(db: Session, sensor: Sensor) -> DBSensor:
    db_network_group = DBNetworkGroup(**sensor.network_group.dict())
    db.add(db_network_group)
    db.flush()

    db_sensor = DBSensor(
      listen_port=sensor.listen_port,
      listen_as_host=sensor.listen_as_host,
      protocol=sensor.protocol,
      description=sensor.description, 
      network_group=db_network_group.id
    )
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)

    return db_sensor


def update(db: Session, sensor: Sensor) -> DBSensor:
    db_network_group = db.query(DBNetworkGroup).filter(DBNetworkGroup.id == sensor.network_group_id).first()
    db_network_group.ip_blocks = sensor.network_group.ip_blocks

    db_sensor = db.query(DBSensor).filter(DBSensor.id == sensor.id).first()
    db_sensor.description = sensor.description
    db_sensor.listen_port = sensor.listen_port
    db_sensor.listen_as_host = sensor.listen_as_host
    db_sensor.protocol = sensor.protocol
    db.add(db_sensor)
    db.commit()

    return db_sensor


def delete(db: Session, id: str):
    db_sensor = db.query(DBSensor).filter(DBSensor.id == id).first()
    db.delete(db_sensor)
    db.commit()

