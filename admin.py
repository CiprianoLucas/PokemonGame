from inicializador_db import InicializadorBD
from batalhas_repositorio import BatalhasRepositorio
from pokemons_repositorio import PokemonsRepositorio
DB_NOME = "pokemons.db"

repositorio_pokemons = PokemonsRepositorio(DB_NOME)
repositorio_batalhas = BatalhasRepositorio(DB_NOME)

InicializadorBD.criar_tabelas(DB_NOME, "pokemons", "id INTEGER PRIMARY KEY AUTOINCREMENT", "nome TEXT NOT NULL", "tipo TEXT NOT NULL", "hp INTEGER NOT NULL")
InicializadorBD.criar_tabelas(DB_NOME, "ataques", "id INTEGER PRIMARY KEY AUTOINCREMENT", "nome TEXT NOT NULL", "dano INTEGER NOT NULL", "tipo TEXT NOT NULL")
InicializadorBD.criar_tabelas(DB_NOME, "ataques_pokemons", "id_pokemon INTEGER", "id_ataque INTEGER", 
                              "FOREIGN KEY('id_ataque') REFERENCES 'ataques', FOREIGN KEY('id_pokemon') REFERENCES 'pokemons'")
InicializadorBD.criar_tabelas(DB_NOME, "batalhas", "id INTEGER PRIMARY KEY AUTOINCREMENT", "id_pokemon_vencedor INTEGER NOT NULL", "id_pokemon_perdedor INTEGER NOT NULL", "data TEXT NOT NULL",
                              "FOREIGN KEY('id_pokemon_vencedor') REFERENCES 'pokemons', FOREIGN KEY('id_pokemon_perdedor') REFERENCES 'pokemons'")

