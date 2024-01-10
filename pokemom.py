from __future__ import annotations
from abc import ABC
from typing import Any, List
from ataque import Ataque
from random import randint
import time

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
        self.__sou_robo = False
        
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
        """Ataca um pokemon com o ataque escolhido usando o índice do ataque

        Args:
            ataque_escolhido (int): indice do ataque escolhido
            pokemon_alvo (Pokemon): pokemon alvo
        """
        dano = self.__verificar_dano(self.ataques[ataque_escolhido], pokemon_alvo)
        dano = int(pokemon_alvo.__esquivar(dano))
        pokemon_alvo.__hp -= dano
        time.sleep(2)
        print(f"""pokemon {pokemon_alvo.nome} recebeu {self.ataques[ataque_escolhido].nome} e levou {dano} de dano""")
        time.sleep(3)
        
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
        """Mostra todos os ataques do pokemon"""
        for i in range(len(self.ataques)):
            print(f"{i + 1}: {self.ataques[i]}")
            
    def ataque_aleatorio(self, pokemon_alvo: Pokemon):
        """Faz um ataque aleatório no pokemon alvo

        Args:
            pokemon_alvo (Pokemon): pokemon que receberá o ataque
        """
        ataque_escolhido = randint(0, 9)
        while ataque_escolhido + 1 > len(pokemon_alvo.ataques):
            ataque_escolhido = randint(0, 9)
        self.atacar(ataque_escolhido, pokemon_alvo)
        
    def __verificar_dano(self, ataque_escolhido: Ataque, pokemon_alvo: Pokemon) -> int:
        """Verifica o dano que vai dar no pokemon alvo com base no tipo do pokemon e to ataque.
        Se forem do mesmo tipo o dano será de 0.8x
        Se tiver vantagem o dano será de 1.2x
        Se tiver desvantagem será de 0.6x

        Args:
            ataque_escolhido (Ataque): Ataque usado
            pokemon_alvo (Pokemon): pokemon que receberá o ataque

        Returns:
            int: _description_
        """
        
        dano = ataque_escolhido.dano * 0.8 if ataque_escolhido.tipo == pokemon_alvo.tipo else ataque_escolhido.dano
        
        lista_tipo =        ["Elétrico", "Venenoso", "Água", "Lutador", "Voador", "Grama", "Inseto", "Fogo", "Psíquico", "Gelo", "Pedra", "Dragão", "Terrestre", "Normal"]
        lista_vantagem =    ["Água", "Lutador", "Terrestre", "Inseto", "Fogo", "Psíquico", "Gelo", "Pedra", "Dragão", "Elétrico", "Venenoso", "Voador", "Grama", "_"]
        lista_desvantagem = ["Pedra","Inseto", "Grama", "Voador", "Dragão", "Fogo", "Água", "Venenoso", "Terrestre", "Psíquico", "Elétrico", "Lutador","Gelo","_"]
        
        indice_tipo = lista_tipo.index(ataque_escolhido.tipo)
        if pokemon_alvo.tipo == lista_vantagem[indice_tipo]:
            dano = dano * 1.2
        if pokemon_alvo.tipo == lista_desvantagem[indice_tipo]:
            dano = dano * 0.6
        
        return dano
    
    def computador(self):
        """Define que o pokemon é jogado por computador"""
        self.__sou_robo = True
        
    def __esquivar(self, dano: int):
        """Entra em um cronômetro onde:
            inserir o número que aparecer dentro de 1 segundo anulará o ataque inimigo
            inserir o número entre 1 e 5 segundos diminuirá o dano dependendo do tempo
            errar o número ou passando mais que 5 segundos receberá dano completo
        """
        time.sleep(2)
        numero_aleatorio = randint(0, 9)
        if not self.__sou_robo:
            print(f"{self.nome}! envie o número que aparecer o mais rápido possível para esquivar")
            time.sleep(4)
            for i in range(3, 0, -1):
                print("." * i)
                time.sleep(1)
            inicio = time.time()
            print(numero_aleatorio, "\n\n")
            numero_digitado = int(input("Número: "))
            fim = time.time()
            tempo = fim - inicio
        else:
            tempo = randint(0, 6)
            numero_digitado = numero_aleatorio
            
        if numero_digitado == numero_aleatorio and tempo <= 1:
            dano = 0
            print("esquivado")
        elif numero_digitado == numero_aleatorio and 1 < tempo < 4.5:
            dano = dano * (tempo - 1) * 0.25 + 1
            print("pegou de raspão")
        else:
            print("pegou em cheio")   
        
        return dano
            
        

            
        
        
        