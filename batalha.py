from abc import ABC
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
           
    def inverter_jogador(self):
        """Alterna entre um jogador e outro"""
        self.__vez = not self.__vez
        if self.__vez:
            print("Vamos lá! sua vez!")
        else:
            print("Vez da máquina")
            
        return self.__vez
        