from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

import flowlytics.sensors.services as services
from flowlytics.database import get_db
from flowlytics.common.exceptions import NotFoundException, ConflictException
from flowlytics.sensors.models import Sensor

router = APIRouter()


@router.get('/', response_model=List[Sensor])
def get_all_sensors(session: Session = Depends(get_db)):
    return services.get_all(session)


@router.get('/{id}', response_model=Sensor)
def get_sensor(id: int, session: Session = Depends(get_db)):
    sensor = services.find_by_id(db=session, id=id)
    if not sensor:
        raise NotFoundException(detail=f"Sensor {id} Not Found")

    return sensor


@router.post('/', response_model=Sensor)
def create_query(sensor: Sensor, session: Session = Depends(get_db)):
    return services.create(session, sensor=sensor)


@router.put('/{id}', response_model=Sensor)
def update_query(id: int, sensor: Sensor, session: Session= Depends(get_db)):
    query = services.find_by_id(db=session, id=id)
    if not query:
        raise NotFoundException(detail=f"Sensor {id} Not Found")
    
    return services.update(db=session, sensor=sensor)


@router.delete('/{id}', response_model=Sensor)
def delete_query(id: int, session: Session = Depends(get_db)):
    sensor = services.find_by_id(db=session, id=id)
    if not sensor:
        raise NotFoundException(detail=f"Sensor {id} Not Found")
    
    return services.delete(db=session, id=id)
