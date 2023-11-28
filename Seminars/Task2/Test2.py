import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_get_token(get_token):
    response = requests.post(url=data["url"], data={"username": data["login"], "password": data["paswd"]})
    res_token = response.json()['token']
    assert res_token == get_token


def test_check_id(get_token, request_get):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(data["url_get"], headers=headers, params={'id': "90418"})
    posts = response.json()
    # print(response.json())
    assert posts == request_get

