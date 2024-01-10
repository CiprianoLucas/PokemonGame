from abc import ABC
import random
from pokemom import Pokemon
import time

class Batalha(ABC):
    """
    Batalha define uma batalha entre um pokemon escolhido pelo usuário e um aleatório
    controledo pelo computador
    
    Atributes:
        nome (str): Nome do animal
        tipo (str): Tipo do pokemon
        hp (int): HP do pokemon
        Ataque (list(Ataque)): ataque do pokemon
    """

    def __init__(self):
           """Inicializa um objeto batalha"""
           self.__vez = bool(random.randint(0, 1))
           self.__fase = 0
           self.__computador = False
           
    def fase(self):
        print("\n")
        time.sleep(2)
        return self.__fase
    
    @property
    def computador(self):
        return self.__computador
           
    def inverter_jogador(self) -> bool:
        """Alterna entre um jogador e outro"""
        self.__vez = not self.__vez
        if self.__vez:
            print("Vez do principal")
        else:
            print("Vez do adversário")
            
        return self.__vez
    
    def pular_fase(self) -> None:
        """Passa para a próxima dafe da batalha,"""
        self.__fase += 1
        time.sleep(1)
        
    def andamento(self) -> bool:
        """Verifica se a batalha passou por todas as fazes e finalizou

        Returns:
            bool: True se batalha não passou se um número específico
        """
        if self.__fase > 2:
            return False
        return True
    
    def contra_computador(self, pokemon: Pokemon):
        """Quando chamado, define que a batalha será duelada contra o computador e qual pokemon é o computador

        Args:
            pokemon (Pokemon): pokemon que será o computador
        """
        self.__computador = True
        pokemon.computador()
        