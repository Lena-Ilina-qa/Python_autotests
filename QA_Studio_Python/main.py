import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e326ea6cfdbb77b9d4ae454ab1a69106'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "i9263939866@yandex.ru",
    "password": "Elizar10"
 }

BODY_CREATE = {
    "name": "Анатолий",
    "photo_id": 1
}

BODY_RENAME = {
    "pokemon_id": "73984",
    "name": "Константин",
    "photo_id": 8
}
BODY_CATCH = {
    "pokemon_id": "73984"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response_create.text)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_RENAME)
print(response_rename.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCH)
print(response_catch.text)
