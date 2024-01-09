from inicializador_db import InicializadorBD
from pokemom import Pokemon
from pokemons_repositorio import PokemonsRepositorio
from ataque import Ataque
from ataques_repositorio import AtaquesRepositorio
from ataque_pokemon_repositorio import AtaquesPokemonRepositorio
from batalha import Batalha
import random

DB_NOME = "pokemons.db"


repositorio_pokemons = PokemonsRepositorio(DB_NOME)
batalha = Batalha()
fase_jogo = 1

pokemon1 = "pikachu"
pokemon2 = "charmander"
pokemon1 = repositorio_pokemons.escolher_pokemon(pokemon1)
pokemon2 = repositorio_pokemons.escolher_pokemon(pokemon2)
print(f"BATALHA: {pokemon1.nome} VS {pokemon2.nome}")


repositorio_pokemons.obter_pokemons()

while True:
    match fase_jogo:
        case 0:
            
            pokemon1 = input("Escolha o seu pokemon: ")
            pokemon2 = input("Escolha o pokemon adversário: ")
            
            try:
                
                pokemon1 = repositorio_pokemons.escolher_pokemon(pokemon1)
                pokemon2 = repositorio_pokemons.escolher_pokemon(pokemon2)
                fase_jogo += 1
                print(f"BATALHA: {pokemon1.nome} VS {pokemon2.nome}")
                
            except:
                print("Não foi encontrado algum dos pokemons selecionados")
                
        case 1:
            if batalha.inverter_jogador():
                pokemon1.mostrar_ataques()
                ataque_escolhido = int(input("escolha seu ataque: "))
                while ataque_escolhido > len(pokemon1.ataques) or ataque_escolhido < 1:
                    print("valor de ataque inválido")
                    ataque_escolhido = int(input("escolha seu ataque: "))

                pokemon1.atacar(ataque_escolhido - 1, pokemon2)
                print(f"""pokemon {pokemon2.nome} recebeu {pokemon1.ataques[ataque_escolhido-1].nome} e levou {pokemon1.ataques[ataque_escolhido-1].dano} de dano""")
                if pokemon2.verificar_vida():
                    fase_jogo += 1
                    print(f"Vitória do {pokemon1.nome}")
                    batalha.finalizar(pokemon1, pokemon2)
                    
            else:
                ataque_escolhido = int(random.randint(0, 9))
                while ataque_escolhido + 1 > len(pokemon2.ataques):
                    ataque_escolhido = int(random.randint(0, 9))
                pokemon2.atacar(ataque_escolhido, pokemon1)
                print(f"""pokemon {pokemon1.nome} recebeu {pokemon2.ataques[ataque_escolhido].nome} e levou {pokemon2.ataques[ataque_escolhido-1].dano} de dano""")
                if pokemon1.verificar_vida():
                    fase_jogo += 1
                    print(f"Vitória do {pokemon2.nome}")
                    batalha.finalizar(pokemon2, pokemon1)

        
                    
        case _:
            break