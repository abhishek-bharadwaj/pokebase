from flask import Flask
from flask import jsonify

from pokedex import public

app = Flask(__name__)


@app.route("/")
def get_pokemons():
    return jsonify(public.get_pokemons())
