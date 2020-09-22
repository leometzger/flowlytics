import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flowlytics.database import SQLBase, get_db
from flowlytics.server import api

from flowlytics.queries.models import CreateQueryRequest, Query, Filters, UpdateQueryRequest
from flowlytics.ipsets.models import CreateIpsetRequest, UpdateIpsetRequest, IpSet



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SQLBase.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

api.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(api)


@pytest.fixture
def ipset():
  return IpSet(id=1, name="testing", ips=['192.168.10.10', '192.168.10.2'])


@pytest.fixture
def ipset_in():
  return CreateIpsetRequest(name="testing", ips=['192.168.10.10', '192.168.10.2'])


@pytest.fixture
def ipset_update():
  return UpdateIpsetRequest(id=1, name="testingv2", ips=['192.168.10.11', '192.168.10.3'])


@pytest.fixture
def filters():
  return Filters(port=80, protocol="tcp")


@pytest.fixture
def query(filters):
  return Query(id=1, name="testing_query", operation="test", filters=filters)


@pytest.fixture
def query_in(filters):
    return CreateQueryRequest(name="testing_query", operation="test", filters=filters)


@pytest.fixture
def query_update(filters):
    return UpdateQueryRequest(id=1, name="testing_queryv2", filters=filters)
