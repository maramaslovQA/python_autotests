import requests
import pytest
token = '5b8889a4138069304c4a340113d2245a'
def test_check_status_code():
    response = requests.get('https://pokemonbattle.me:9104/pokemons', headers = {'trainer_token': token})
    assert response.status_code == 200

def test_check_trainerid():
    response = requests.get('https://pokemonbattle.me:9104/trainers',
                             params = {'trainer_id': 2136}) 
    assert response.json()['trainer_name'] == 'Kobi'   