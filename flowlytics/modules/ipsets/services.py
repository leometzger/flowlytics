from pymongo.database import Database
from bson.objectid import ObjectId
from .entities import IpSet

COLLECTION_NAME = 'ipsets'

def get_all(db: Database):
  docs = db[COLLECTION_NAME].find()
  ipsets = []

  for doc in docs:
    ipsets.append(IpSet(id=str(doc['_id']), **doc))

  return ipsets


def find_by_id(id: str, db: Database):
  doc = db[COLLECTION_NAME].find_one({"_id": ObjectId(id)})

  return IpSet(id=str(doc['_id']), **doc) 


def create(ipset: IpSet, db: Database) -> IpSet:
  doc = db[COLLECTION_NAME].insert_one({ 
    "name": ipset.name, 
    "ips": ipset.ips 
  })

  return IpSet(id=str(doc.inserted_id), **doc)


def update(id: str, ipset: IpSet, db: Database):
  doc = db[COLLECTION_NAME].update_one(
    {"_id": ObjectId(id)},
    {
      "$set": {
        "name": ipset.name,
        "ips": ipset.ips
      }
    }
  )

  return ipset.


def delete(id: str, db: Database):
  result = db[COLLECTION_NAME].delete_one({"_id": ObjectId(id)})
  print(result.deleted_count)

