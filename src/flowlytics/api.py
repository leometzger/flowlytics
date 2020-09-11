from fastapi import APIRouter

from flowlytics.database import database
from flowlytics.modules.ipsets import router as ipsets_router
from flowlytics.modules.queries import router as queries_router

router = APIRouter()


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


router.include_router(ipsets_router, prefix='/ipsets', tags=['ipsets'])
router.include_router(queries_router, prefix='/queries', tags=['queries'])