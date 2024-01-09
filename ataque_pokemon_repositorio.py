from typing import Any, List
import sqlite3
from pokemom import Pokemon
from ataque import Ataque

class AtaquesPokemonRepositorio:
    "Repositório de ataques relacionados a um pokemon"
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        
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
           
    def inserir_ataque(self, ataque: Ataque, pokemon: Pokemon) -> None:
        """Insere um ataque de um pokemon no banco de dados.
        
        Args:
            ataque (Ataque): ataque selecionado.
            pokemon (Pokemon): pokemon que terá o ataque
        """
        query = "INSERT INTO ataques_pokemons (id_ataque, id_pokemon) VALUES (?, ?)"
        self.__executar_query(query, ataque.id, pokemon.id)

    def remover_ataque(self, ataque: Ataque, pokemon: Pokemon) -> None:
        """Remove um ataque do banco de dados."""
        query = "DELETE FROM ataques_pokemons WHERE id_ataque = ? AND id_pokemon = ?"
        self.__executar_query(query, ataque.id, pokemon.id)

    def obter_ataques_pokemon(self, pokemon: str) -> List[Ataque]:
        """Obtém todos os ataques cadastrados no banco de dados de um Pokémon."""
        query = f"""SELECT ataques.id, ataques.nome, ataques.dano, ataques.tipo
                    FROM ataques
                    JOIN ataques_pokemons ON ataques.id = ataques_pokemons.id_ataque
                    JOIN pokemons ON ataques_pokemons.id_pokemon = pokemons.id
                    WHERE LOWER(pokemons.nome) = LOWER(?)"""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, (pokemon,))
        rows = cursor.fetchall()
        connection.close()

        # Corrigir a indexação dos resultados
        return [Ataque(row[1], row[2], row[3], row[0]) for row in rows]