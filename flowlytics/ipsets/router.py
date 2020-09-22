import flowlytics.ipsets.services as services
from flowlytics.ipsets.models import IpSet, CreateIpsetRequest, UpdateIpsetRequest
from flowlytics.common.exceptions import ConflictException, NotFoundException
from flowlytics.database import get_db

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.get('/', response_model=List[IpSet])
def get_ipsets(session: Session= Depends(get_db)):
    return services.get_all(session)



@router.get('/{id}', response_model=IpSet)
def get_ipset(id: int, session: Session = Depends(get_db)):
    ipset = services.find_by_id(db=session, id=id)
    if ipset is None:
        raise NotFoundException(detail=f"Ipset {id} Not Found")

    return ipset


@router.post('/', response_model=IpSet)
def create_ipset(request: CreateIpsetRequest, session: Session = Depends(get_db)):
    ipset = IpSet(id=None, name=request.name, ips=request.ips)
    is_duplicated = services.find_by_name(session, ipset.name)

    if is_duplicated is not None:
        raise ConflictException(detail="Duplicated name")

    return services.create(session, ipset)


@router.put('/{id}', response_model=IpSet)
def update_ipset(id: int, request: UpdateIpsetRequest, session: Session= Depends(get_db)):
    ipset = services.find_by_id(db=session, id=id)
    if not ipset:
        raise NotFoundException(detail=f"Ipset {id} Not Found")
    
    ipset = IpSet(id=id, name=request.name, ips=request.ips)
    return services.update(db=session, ipset=ipset)


@router.delete('/{id}')
def delete_ipset(id: int, session: Session = Depends(get_db)):
    ipset = services.find_by_id(db=session, id=id)
    if not ipset:
        raise NotFoundException(detail=f"Ipset {id} Not Found")
    
    return services.delete(db=session, id=id)

