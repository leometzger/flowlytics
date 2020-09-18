from sqlalchemy.orm import Session
from flowlytics.database.tables import DBIpSet

from .models import IpSet

SEPARATOR = ':'

def decode_db_ipset(db_ipset: DBIpSet) -> IpSet:
    if db_ipset is None:
        return None

    ips = db_ipset.ips.split(SEPARATOR)
    ipset = IpSet(id=db_ipset.id, name=db_ipset.name, ips=ips)
    return ipset


def encode_ipset(ipset: IpSet) -> DBIpSet:
    db_ipset = DBIpSet(name=ipset.name, ips=SEPARATOR.join(ipset.ips))
    return db_ipset


def get_all(db: Session):
    results = db.query(DBIpSet).all()
    return list(map(results, decode_db_ipset))


def find_by_id(db: Session, id: str):
    db_ipset = db.query(DBIpSet).filter(DBIpSet.id == id).first()
    return decode_db_ipset(db_ipset)


def find_by_name(db: Session, name: str):
    db_ipset = db.query(DBIpSet).filter(DBIpSet.name == name).first()
    return decode_db_ipset(db_ipset)


def create(db: Session, ipset: IpSet) -> IpSet:
    db_ipset = DBIpSet(name=ipset.name, ips=SEPARATOR.join(ipset.ips))
    db.add(db_ipset)
    db.commit()
    db.refresh(db_ipset)
    return decode_db_ipset(db_ipset)


def update(db: Session, ipset: IpSet):
    db_ipset = db.query(DBIpSet).filter(DBIpSet.id == ipset.id).first()
    db_ipset.name = ipset.name
    db_ipset.ips = SEPARATOR.join(ipset.ips)

    db.add(db_ipset)
    db.commit()

    return decode_db_ipset(db_ipset)


def delete(db: Session, id: str):
    db_ipset = db.query(DBIpSet).filter(DBIpSet.id == id).first()
    db.delete(db_ipset)
    db.commit()
