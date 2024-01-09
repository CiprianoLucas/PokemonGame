import sqlite3

class InicializadorBD:
    """Classe responsável por iniciar o banco de dados."""
    @staticmethod
    def criar_tabelas(db_nome: str, nome: str ,*colunas_tipos: str):
        """Cria as tabelas no banco de dados.

        Args:
            db_nome (str): Nome do banco de dados.
            nome (str): Nome da tabela
            colunas_tipos (str): Nome de cada coluna com seu tipo de variável
            
        """
        query = f'''CREATE TABLE IF NOT EXISTS {nome} ('''
                 
        for i, coluna_tipo in enumerate(colunas_tipos):
            if i != len(colunas_tipos) - 1:
                query += f'{coluna_tipo}, '
            else:
                query += f'{coluna_tipo}'
        
        query += ');'
        
        print(query)

        connection = sqlite3.connect(db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()