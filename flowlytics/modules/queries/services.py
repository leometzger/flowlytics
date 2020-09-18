from sqlalchemy.orm import Session
from flowlytics.database.tables import DBQuery
from flowlytics.modules.queries.models import Query


def get_all(db: Session):
    results = db.query(DBQuery).all()
    return results


def find_by_id(db: Session, id: str):
    db_query = db.query(DBQuery).filter(DBQuery.id == id).first()
    return Query(**db_query)


def find_by_name(db: Session, name: str):
    db_query = db.query(DBQuery).filter(DBQuery.name == name).first()
    return Query(**db_query)


def create(db: Session, query: Query) -> Query:
    db_query = DBQuery(**query)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    query.id = db_query.id
    return query


def update(db: Session, query: Query):
    db_query = db.query(DBQuery).filter(DBQuery.id == query.id).first()
    db_query.name = query.name
    db.add(db_query)
    db.commit()

    return Query(**db_query)


def delete(db: Session, id: str):
    db_query = db.query(DBQuery).filter(DBQuery.id == id).first()
    db.delete(db_query)
    db.commit()
