import pytest

from flowlytics.queries.models import Query
from flowlytics.queries.models import CreateQueryRequest, Query, Filters, UpdateQueryRequest

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



def test_create_query(client, query, query_in):
  response = client.post('/api/queries/', json=query_in.dict())

  assert response.status_code == 200
  assert response.json() == query.dict()


def test_create_query_duplicated_name(client, query_in):
  response = client.post('/api/queries/', json=query_in.dict())

  assert response.status_code == 409


def test_get_all_queries(client, query):
  response = client.get('/api/queries/')

  assert response.status_code == 200
  assert response.json() == [query.dict()]


def test_get_query(client, query):
  response = client.get('/api/queries/1')

  assert response.status_code == 200
  assert response.json() == query.dict()


def test_get_inexistent_query(client):
  response = client.get('/api/queries/10')

  assert response.status_code == 404


def test_update_query(client, query, query_update):
  response = client.put('/api/queries/1', json=query_update.dict())

  assert response.status_code == 200
  assert response.json()['name'] == 'testing_queryv2'


def test_update_inexistent_query(client, query_update):
  response = client.put('/api/queries/10', json=query_update.dict())

  assert response.status_code == 404


def test_delete_query(client):
  response = client.delete('/api/queries/1')
  resp_get = client.get('/api/queries/1')

  assert response.status_code == 200
  assert resp_get.status_code == 404
 