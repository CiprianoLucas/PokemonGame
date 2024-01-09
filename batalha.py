from abc import ABC
from ataque import Ataque
from pokemom import Pokemon
import random

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
           
    def finalizar(self, pokemon1: Pokemon, pokemon2: Pokemon):
        """Finaliza a batalha definindo o vencedor e o perdedor

        Args:
            pokemon1 (Pokemon): pokemon vencedor
            pokemon2 (Pokemon): pokemon perdedor"""

        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2

    def inverter_jogador(self):
        """Alterna entre um jogador e outro"""
        self.__vez = not self.__vez
        if self.__vez:
            print("Vamos lá! sua vez!")
        else:
            print("Vez da máquina")
            
        return self.__vez
        