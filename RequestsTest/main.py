import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a62dbe7c6b9e69290fc8473c0c444178'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "69518",
    "name": "New Name",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "69518"
}

'''responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (responce_create.text)'''

'''responce_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print (responce_name.text)'''

'''responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (responce_pokeball.text)'''
