from fastapi import APIRouter, Depends
from pymongo.database import Database
from flowlytics.database import get_db

router = APIRouter()

@router.get('/')
def get_all_queries(db: Database = Depends(get_db)):
    pass


@router.get('/{id}')
def get_query(id: str, db: Database = Depends(get_db)):
    pass


@router.post('/')
def create_query():
    pass


@router.put('/{id}')
def update_query():
    pass


@router.delete('/{id}')
def delete_query():
    pass