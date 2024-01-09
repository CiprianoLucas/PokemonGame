from abc import ABC


class Ataque(ABC):
    """
    Ataque representa um tipo de ataque
    
    Atributes:
        nome(str): nome do ataque do pokemon
        dano(int): dano do ataque do pokemon
        tipo(str): tipo do ataque do pokemon
    """

    def __init__(self, nome: str, dano: int, tipo: str, id: int = None):
        """Cria um objeto ataque

        Args:
            nome (str): nome do ataque
            dano (int): dano do ataque
            tipo (str): tipo do ataque
            id (int, optional): id no banco de dados. Defaults to None.
        """
        self.__nome = nome
        self.__dano = dano
        self.__tipo = tipo
        self.__id = id
    
    def __str__(self):
        return f"{self.nome} dano:{self.dano}"
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def dano(self):
        return self.__dano
    
    @property
    def id(self):
        return self.__id