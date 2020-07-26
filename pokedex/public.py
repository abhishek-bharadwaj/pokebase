import requests

from functools import lru_cache

import pokebase as pb


@lru_cache(maxsize=10)
def get_pokemons(limit=10):
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit={}'.format(limit))
    if r.status_code != 200:
        return
    pokemons = r.json()['results']
    for pokemon in pokemons:
        pokemon['image'] = pb.pokemon(pokemon['name']).sprites.front_default
    return pokemons
