from fastapi import APIRouter, Depends

from .models import IpSet, CreateIpsetRequest, UpdateIpsetRequest

router = APIRouter()


@router.get('/')
async def get_ipsets():
    return [], 200


@router.get('/{id}', response_model=IpSet)
async def get_ipset():
    # return find_by_id(id=id)
    return 200


@router.post('/', response_model=IpSet)
async def post_ipset(request: CreateIpsetRequest):
    #ipset = IpSet(*request)
    # if ipset.some_duplicated:
    #    return 400, {"message": "Duplicated IP in ipset"}

    # return create(ipset=ipset)
    return 200


@router.put('/{id}', response_model=IpSet)
async def put_ipset():
    # if ipset.some_duplicated:
    #    return 400, {"message": "Duplicated IP in ipset"}
    # return update(id=id, ipset=ipset, db=db)
    return 200


@router.delete('/{id}', response_model=IpSet)
async def delete_ipset():
    #delete(id=id, db=db)
    return 200


@router.post('/{id}/ips')
async def add_ip(ip: str):
    return 200
