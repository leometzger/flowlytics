import flowlytics.modules.ipsets.services as services

from fastapi import APIRouter, Depends, HTTPException
from flowlytics.database import get_db
from sqlalchemy.orm import Session
from typing import List

from .models import IpSet, CreateIpsetRequest, UpdateIpsetRequest


router = APIRouter()


@router.get('/', response_model=List[IpSet])
def get_ipsets(session: Session= Depends(get_db)):
    ipsets = services.get_all(session)
    return ipsets



@router.get('/{id}', response_model=IpSet)
def get_ipset(id: int, session: Session = Depends(get_db)):
    ipset = services.find_by_id(db=session, id=id)
    if ipset is None:
        raise HTTPException(404, detail="Ipset Not Found")

    return ipset


@router.post('/', response_model=IpSet)
def create_ipset(request: CreateIpsetRequest, session: Session = Depends(get_db)):
    ipset = IpSet(id=None, name=request.name, ips=request.ips)
    is_duplicated = services.find_by_name(session, ipset.name)

    if is_duplicated is not None:
        raise HTTPException(409, detail="Duplicated name")

    return services.create(session, ipset)


@router.put('/{id}', response_model=IpSet)
def update_ipset(id: int, request: UpdateIpsetRequest, session: Session= Depends(get_db)):
    ipset = IpSet(id=id, name=request.name, ips=request.ips)

    return services.update(db=session, ipset=ipset)


@router.delete('/{id}')
def delete_ipset(id: int, session: Session = Depends(get_db)):
    services.delete(db=session, id=id)
    return 204


@router.post('/{id}/ips')
def add_ip(ip: str, session: Session = Depends(get_db)):
    return 200
