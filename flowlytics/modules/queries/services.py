from sqlalchemy.orm import Session
from flowlytics.database.tables import DBQuery, DBFilter
from flowlytics.modules.queries.models import Query
from typing import List


def get_all(db: Session) -> List[DBQuery]:
    return db.query(DBQuery).all()


def find_by_id(db: Session, id: str) -> DBQuery:
    return db.query(DBQuery).filter(DBQuery.id == id).first()


def find_by_name(db: Session, name: str) -> DBQuery:
    db_query = db.query(DBQuery).filter(DBQuery.name == name).first()
    if not db_query:
        return None
    return db_query


def create(db: Session, query: Query) -> DBQuery:
    db_filter = DBFilter()
    db_filter.start_date = query.filters.start_date
    db_filter.end_date = query.filters.end_date
    db_filter.port = query.filters.port
    db_filter.protocol = query.filters.protocol

    db.add(db_filter)
    db.flush()

    db_query = DBQuery(id=query.id, name=query.name, filters=db_filter)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)

    return db_query


def update(db: Session, query: Query) -> DBQuery:
    db_query = db.query(DBQuery).filter(DBQuery.id == query.id).first()
    db_query.name = query.name
    db.add(db_query)
    db.commit()

    return db_query


def delete(db: Session, id: str):
    db_query = db.query(DBQuery).filter(DBQuery.id == id).first()
    db.delete(db_query)
    db.commit()
