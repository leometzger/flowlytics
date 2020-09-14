from fastapi import APIRouter, Depends
from flowlytics.database import get_db, FlowlyticsDb

from .models import IpSet, CreateIpsetRequest, UpdateIpsetRequest
from .services import get_all

router = APIRouter()


@router.get('/')
async def get_ipsets(db: FlowlyticsDb = Depends(get_db)):
    # result = await get_all(db=db)
    result = db.ipsets.select()
    return result.


@router.get('/{id}', response_model=IpSet)
async def get_ipset(db: FlowlyticsDb = Depends(get_db)):
    # return find_by_id(id=id)
    return 200


@router.post('/', response_model=IpSet)
async def post_ipset(request: CreateIpsetRequest, db: FlowlyticsDb = Depends(get_db)):
    #ipset = IpSet(*request)
    # if ipset.some_duplicated:
    #    return 400, {"message": "Duplicated IP in ipset"}

    # return create(ipset=ipset)
    return 200


@router.put('/{id}', response_model=IpSet)
async def put_ipset(db: FlowlyticsDb = Depends(get_db)):
    # if ipset.some_duplicated:
    #    return 400, {"message": "Duplicated IP in ipset"}
    # return update(id=id, ipset=ipset, db=db)
    return 200


@router.delete('/{id}', response_model=IpSet)
async def delete_ipset(db: FlowlyticsDb = Depends(get_db)):
    #delete(id=id, db=db)
    return 200


@router.post('/{id}/ips')
async def add_ip(ip: str, db: FlowlyticsDb = Depends(get_db)):
    return 200
