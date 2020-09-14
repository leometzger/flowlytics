from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/')
async def get_all_queries():
    return [], 200


@router.get('/{id}')
async def get_query():
    return 200


@router.post('/')
async def create_query():
    return 200


@router.put('/{id}')
async def update_query():
    return 200


@router.delete('/{id}')
async def delete_query():
    return 200
