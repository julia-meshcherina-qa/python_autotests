import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '4ade5b391ecfdc15e62a1f9aa73d82c4' }
TOKEN = '4ade5b391ecfdc15e62a1f9aa73d82c4'

body1 = {
    "name": "Kira",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body2 = {
    "pokemon_id": "16844",
    "name": "Helen",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}

body3 = {
    "pokemon_id": "16844"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body1)

print(response.text)

response.confirm = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body2)

print(response.confirm.text)

response.confirm1 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body3)

print(response.confirm1.text)
