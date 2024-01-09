from typing import Any, List
from pokemom import Pokemon
import sqlite3
from datetime import date

class BatalhasRepositorio:
    "Repositório de Batalhas"
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
        
    def __get_ultimo_id_inserido(self) -> int:        
        """Retorna o ID do último registro inserido no banco de dados."""
        query = "SELECT id FROM batalhas ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
    
    def inserir_batalha(self, pokemon1: Pokemon, pokemon2: Pokemon):
        """Insere uma batalha no banco de dados. O objeto ataque é atualizado com o ID do banco.
        
        Args:
            pokemon1 (Pokemon): pokemon que venceu.
            pokemon2 (Pokemon): Pokemon que perdeu.
        """
        query = "INSERT INTO batalhas (id_pokemon_vencedor, id_pokemon_perdedor, data) VALUES (?, ?, ?)"
        self.__executar_query(query, pokemon1.id, pokemon2.id, date.today())

    def remover_batalha(self, id: int) -> None:
        """Remove um ataque do banco de dados."""
        query = "DELETE FROM ataques WHERE id = ?"
        self.__executar_query(query, id)

    def obter_batalhas(self) -> List[str]:
        """Obtém todas as batalhas cadastrados no banco de dados."""
        query = "SELECT * FROM batalhas"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [(row[0], row[1], row[2], row(3)) for row in rows]