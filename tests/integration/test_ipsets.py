import pytest
from flowlytics.ipsets.models import IpSet

def test_create_ipset(client, ipset, ipset_in):
  response = client.post('/api/ipsets/', json=ipset_in.dict())

  assert response.status_code == 200
  assert response.json() == ipset.dict()


def test_create_ipset_duplicated_name(client, ipset_in):
  response = client.post('/api/ipsets/', json=ipset_in.dict())

  assert response.status_code == 409
 

#def test_get_all_ipsets(client, ipset):
#  response = client.get('/api/ipsets/')
#
#  assert response.status_code == 200
#  assert response.json() == [ipset.dict()]


def test_get_ipset(client, ipset):
  response = client.get('/api/ipsets/1')

  assert response.status_code == 200
  assert response.json() == ipset.dict()


def test_get_inexistent_ipset(client):
  response = client.get('/api/ipsets/10')

  assert response.status_code == 404


def test_update_ipset(client, ipset, ipset_update):
  response = client.put('/api/ipsets/1', json=ipset_update.dict())

  assert response.status_code == 200
  assert response.json() == IpSet(**ipset_update.dict()).dict()


def test_update_inexistent_ipset(client):
  json = {"id": 10, "name": 'testingv2', "ips": ['192.168.10.11', '192.168.10.3']}
  response = client.put('/api/ipsets/10', json=json)

  assert response.status_code == 404


def test_delete_ipset(client):
  response = client.delete('/api/ipsets/1')
  resp_get = client.get('/api/ipsets/1')

  assert response.status_code == 200
  assert resp_get.status_code == 404
 