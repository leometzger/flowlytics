from flowlytics.database import FlowlyticsDb

from .models import IpSet


async def get_all(db: FlowlyticsDb):
    testing = db.ipsets.select()
    return testing


async def find_by_id(id: str, db: FlowlyticsDb):
    print('finded')
    return IpSet(id=1, name="testing", ips=['192.168.0.1'])


async def create(ipset: IpSet, db: FlowlyticsDb) -> IpSet:
    print('created')
    return IpSet(id=1, name="testing", ips=['192.168.0.1'])


async def update(id: str, ipset: IpSet, db: FlowlyticsDb):
    print('updated')
    return IpSet(id=1, name="testing", ips=['192.168.0.1'])


async def delete(id: str, db: FlowlyticsDb):
    print('deleted')
    return IpSet(id=1, name="testing", ips=['192.168.0.1'])
