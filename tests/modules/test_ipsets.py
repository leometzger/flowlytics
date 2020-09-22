from flowlytics.ipsets.models import CreateIpsetRequest, UpdateIpsetRequest

from ..conftest import client


def test_create_ipset():
  json = {"name": 'testing', "ips": ['192.168.10.10', '192.168.10.2']}
  response = client.post('/api/ipsets/', json=json)
  data = response.json()

  assert response.status_code == 200
  assert data["id"] == 1
  assert data["name"] == "testing"
