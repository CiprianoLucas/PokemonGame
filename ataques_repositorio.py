from typing import Any, List
import sqlite3
from pokemom import Pokemon
from ataque import Ataque

class AtaquesRepositorio:
    "Repositório de Ataques"
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
        query = "SELECT id FROM ataques ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
    
    def inserir_ataque(self, ataque: Ataque) -> Ataque:
        """Insere um ataque no banco de dados. O objeto ataque é atualizado com o ID do banco.
        
        Args:
            ataque (Ataque): ataque que será criado.
        """
        query = "INSERT INTO ataques (nome, dano, tipo) VALUES (?, ?, ?)"
        self.__executar_query(query, ataque.nome, ataque.dano, ataque.tipo)

        ataque_id = self.__get_ultimo_id_inserido()
        ataque.id = ataque_id
        return ataque

    def atualizar_ataque(self, ataque: Ataque) -> None:
        """Atualiza os dados de um ataque no banco de dados."""
        query = "UPDATE ataques SET nome = ?, dano = ?, tipo = ? WHERE id = ?"
        self.__executar_query(query, ataque.nome, ataque.dano, ataque.tipo, ataque.id)

    def remover_ataque(self, ataque: Ataque) -> None:
        """Remove um ataque do banco de dados."""
        query = "DELETE FROM ataques WHERE id = ?"
        self.__executar_query(query, ataque.id)            
        
    def obter_ataque(self) -> List[Ataque]:
        """Obtém todos os ataques cadastrados no banco de dados."""
        query = "SELECT * FROM ataques"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Ataque(row[0], row[1], row[2], row(3)) for row in rows]