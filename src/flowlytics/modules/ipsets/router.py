from fastapi import APIRouter, Depends

from .models import IpSet, CreateIpsetRequest, UpdateIpsetRequest
from .services import get_all, find_by_id, create, update, delete

router = APIRouter()

@router.get('/')
async def get_ipsets():
    return get_all()


@router.get('/{id}', response_model=IpSet)
async def get_ipset():
    return find_by_id(id=id, db=db)


@router.post('/', response_model=IpSet)
async def post_ipset(request: CreateIpsetRequest):
    if ipset.some_duplicated:
        return 400, {"message": "Duplicated IP in ipset"}
    return create(ipset=ipset, db=db)


@router.put('/{id}', response_model=IpSet)
async def put_ipset():
    if ipset.some_duplicated:
        return 400, {"message": "Duplicated IP in ipset"}
    return update(id=id, ipset=ipset, db=db)


@router.delete('/{id}', response_model=IpSet)
async def delete_ipset():
    delete(id=id, db=db)
    return 200


@router.post('/{id}/ips')
async def add_ip(ip: str):
    return 200