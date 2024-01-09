from typing import Any, List
import sqlite3
from pokemom import Pokemon
from ataque import Ataque
from ataque_pokemon_repositorio import AtaquesPokemonRepositorio

class PokemonsRepositorio:
    "Repositório de Pokemons"
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.__ataques_repositorio = AtaquesPokemonRepositorio(db_name)
        
    def __executar_query(self, query: str, *params: Any) -> None:
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
        
    def __get_ultimo_id_inserido(self) -> int:        
        """Retorna o ID do último registro inserido no banco de dados."""
        query = "SELECT id FROM pokemons ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
    
    def inserir_pokemon(self, pokemon: Pokemon) -> Pokemon:
        """Insere um pokemon no banco de dados. O objeto pokemon é atualizado com o ID do banco.
        
        Args:
            pokemon (Pokemon): pokemon que será criado.
        """
        query = "INSERT INTO pokemons (nome, tipo, hp) VALUES (?, ?, ?)"
        self.__executar_query(query, pokemon.nome, pokemon.tipo, pokemon.hp)

        pokemon_id = self.__get_ultimo_id_inserido()
        pokemon.id = pokemon_id
        
        
        
        pokemon.ataques
        return pokemon

    def atualizar_pokemon(self, pokemon: Pokemon) -> None:
        """Atualiza os dados de um pokemon no banco de dados."""
        query = "UPDATE pokemons SET nome = ?, tipo = ?, hp = ? WHERE id = ?"
        self.__executar_query(query, pokemon.nome, pokemon.tipo, pokemon.hp, pokemon.id)

    def remover_pokemon(self, pokemon: Pokemon) -> None:
        """Remove um pokemon do banco de dados."""
        query = "DELETE FROM pokemons WHERE id = ?"
        self.__executar_query(query, pokemon.id)

    def obter_pokemons(self) -> List[Pokemon]:
        """Obtém todos os pokemons cadastrados no banco de dados."""
        query = "SELECT * FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        pokemons = [Pokemon(row[1], row[2], row[3], row[0]) for row in rows]
        for i in range(len(pokemons)):
            print(pokemons[i])
    
    def escolher_pokemon(self, pokemon: str) -> Pokemon:
        """Obtém um pokemon do banco de dados."""
        query = "SELECT * FROM pokemons WHERE LOWER(nome) = LOWER(?)"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, (pokemon,))
        rows = cursor.fetchall()
        connection.close()
        Obj_pokemon = Pokemon(rows[0][1], rows[0][2], rows[0][3], rows[0][0], self.__ataques_repositorio.obter_ataques_pokemon(pokemon))
        return Obj_pokemon
