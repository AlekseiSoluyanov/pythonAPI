import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    res = requests.post(url=data["url"], data={"username": data["login"], "password": data["paswd"]})
    token = res.json()["token"]
    return token


@pytest.fixture()
def request_get(get_token):
    res_get = requests.get(url=data["url_get"], headers={"X-Auth-Token": get_token}, params={"id": "90418"})
    return res_get.json()

