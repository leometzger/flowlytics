from fastapi import APIRouter, Depends

from flowlytics.database import database, get_db
from flowlytics.ipsets.router import router as ipsets_router
from flowlytics.queries.router import router as queries_router

router = APIRouter()


@router.on_event("startup")
def startup():
    pass


@router.on_event("shutdown")
def shutdown():
    pass


router.include_router(
    ipsets_router,
    prefix='/ipsets',
    tags=['ipsets']
)
router.include_router(
    queries_router,
    prefix='/queries',
    tags=['queries']
)
