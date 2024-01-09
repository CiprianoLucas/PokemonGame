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
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.id = id
    
    def __str__(self):
        return f"{self.nome} dano:{self.dano}"