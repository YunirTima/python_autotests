import requests
import pytest

import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a62dbe7c6b9e69290fc8473c0c444178'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5423'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_responce():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "CATBattle"