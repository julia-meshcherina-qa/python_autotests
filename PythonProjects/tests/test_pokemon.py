import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '4ade5b391ecfdc15e62a1f9aa73d82c4' }
TOKEN = '4ade5b391ecfdc15e62a1f9aa73d82c4'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"level" : 1})
    assert response.status_code == 200 

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2638})
    assert response.json()['data'][0]['trainer_name'] == 'Julia'