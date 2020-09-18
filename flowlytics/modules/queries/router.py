import flowlytics.modules.queries.services as services

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from flowlytics.modules.queries.models import Query, CreateQueryRequest, UpdateQueryRequest
from flowlytics.database import get_db
from flowlytics.common.exceptions import NotFoundException, ConflictException

router = APIRouter()


@router.get('/', response_model=List[Query])
def get_all_queries(session: Session = Depends(get_db)):
    return services.get_all(session)


@router.get('/{id}', response_model=Query)
def get_query(id: int, session: Session = Depends(get_db)):
    query = services.find_by_id(db=session, id=id)
    if not query:
        raise NotFoundException(detail=f"Query {id} Not Found")

    return query


@router.post('/', response_model=Query)
def create_query(request: CreateQueryRequest, session: Session = Depends(get_db)):
    query = Query(id=None, name=request.name, filters=request.filters)
    is_duplicated = services.find_by_name(session, query.name)
    if is_duplicated is not None:
        raise ConflictException(detail="Duplicated name")

    return services.create(session, query)


@router.put('/{id}', response_model=Query)
def update_query(id: int, request: UpdateQueryRequest, session: Session= Depends(get_db)):
    query = services.find_by_id(db=session, id=id)
    if not query:
        raise NotFoundException(detail=f"Query {id} Not Found")
    
    query = Query(id=id, name=request.name, filters=query.filters)
    return services.update(db=session, query=query)


@router.delete('/{id}')
def delete_query(id: int, session: Session = Depends(get_db)):
    query = services.find_by_id(db=session, id=id)
    if not query:
        raise NotFoundException(detail=f"Query {id} Not Found")
    
    return services.delete(db=session, id=id)
