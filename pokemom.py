from __future__ import annotations
from abc import ABC
from typing import Any, List
from ataque import Ataque

class Pokemon(ABC):
    """
    Pokemon representa um tipo de pokemon
    
    Atributes:
        nome (str): Nome do animal
        tipo (str): Tipo do pokemon
        hp (int): HP do pokemon
        Ataque (list(Ataque)): ataque do pokemon
    """

    def __init__(self, nome: str, tipo: str, hp: int, id: int = None, ataques: List = [Ataque]):
        """inicializa um Pokemon

        Args:
            nome (str): Nome do Pokemon
            tipo (str): Tipo do Pokemon
            hp (int): Vida do Pokemon
            id (int, optional): id do pokemon.
            ataques (list[Ataques], optional): ataques que o pokemon tem.
            
        """
        self.__nome = nome
        self.__tipo = tipo
        self.__hp = hp
        self.__id = id
        self.__ataques = ataques
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def hp(self):
        return self.__hp
    
    @property
    def id(self):
        return self.__id
    
    @property
    def ataques(self):
        return self.__ataques
        
    def __str__(self):
        return f"""nome: {self.nome} | tipo: {self.tipo} | hp: {self.hp}"""
        
    def atacar(self, ataque_escolhido: int, pokemon_alvo: Pokemon):
        pokemon_alvo.__hp -= self.ataques[ataque_escolhido].dano
        
    def verificar_vida(self) -> bool:
        """Verifica a vida do pokemon e retorna se está com vida zero ou menor

        Returns:
            bool: True se estiver com 0 ou menos de vida
        """
        if self.hp <= 0:
            self.__hp = 0
            print(f"Pokemon {self.nome} está inconciente")
            return True
        print(f"Pokemon {self.nome} está com {self.hp} de HP")
        return False
    
    def mostrar_ataques(self) -> None:
        for i in range(len(self.ataques)):
            print(f"{i + 1}: {self.ataques[i]}")
        