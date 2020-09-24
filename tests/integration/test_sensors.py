import pytest

from flowlytics.sensors.models import Sensor, NetworkGroup

@pytest.fixture
def network_group():
  return NetworkGroup(id=1, ip_blocks=['192.168.0.0/24', '172.16.0.0/16'])

@pytest.fixture
def network_group_in():
  return NetworkGroup(ip_blocks=['192.168.0.0/24', '172.16.0.0/16'])


@pytest.fixture
def sensor(network_group):
  return Sensor(
    description="testing",  
    protocol="tcp",
    listen_as_host="127.0.0.1",
    listen_port=10000,
    network_group=network_group
  )


@pytest.fixture
def sensor_in(network_group_in):
  return Sensor(
    description="testing",  
    protocol="tcp",
    listen_as_host="127.0.0.1",
    listen_port=10000,
    network_group=network_group_in
  )


def test_create_sensor(client, sensor, sensor_in):
  response = client.post('/api/sensors/', json=sensor_in.dict())

  assert response.status_code == 201
  assert response.json() == sensor.dict()


def test_create_sensor_duplicated_name(client, sensor_in):
  response = client.post('/api/sensors/', json=sensor_in.dict())

  assert response.status_code == 409
 

#def test_get_all_sensors(client, sensor):
#  response = client.get('/api/sensors/')
#
#  assert response.status_code == 200
#  assert response.json() == [sensor.dict()]


def test_get_sensor(client, sensor):
  response = client.get('/api/sensors/1')

  assert response.status_code == 200
  assert response.json() == sensor.dict()


def test_get_inexistent_sensor(client):
  response = client.get('/api/sensors/10')

  assert response.status_code == 404


def test_update_sensor(client, sensor):
  response = client.put('/api/sensors/1', json=sensor.dict())

  assert response.status_code == 200
  assert response.json() == sensor.dict()


def test_update_inexistent_sensor(client, sensor):
  json = sensor.dict()
  json.id = 10
  response = client.put('/api/sensors/10', json=json)

  assert response.status_code == 404


def test_delete_sensor(client):
  response = client.delete('/api/sensors/1')
  resp_get = client.get('/api/sensors/1')

  assert response.status_code == 200
  assert resp_get.status_code == 404
 