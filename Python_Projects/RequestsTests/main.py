import requests

token = '5b8889a4138069304c4a340113d2245a'

response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token': token},
                         json = {"name":"Poker", "photo":"https://dolnikov.ru/pokemons/albums/079.png"})
print (response.text)

change_pokemon_name = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token': token},
                         json = {'pokemon_id': '6038', 'name':'Puna', 'photo':'https://dolnikov.ru/pokemons/albums/091.png'})
print (change_pokemon_name.text)

add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 'trainer_token': token},
                         json = {'pokemon_id': '6038'})
print(add_pokeball.text)