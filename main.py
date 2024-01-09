from pokemons_repositorio import PokemonsRepositorio
from batalha import Batalha
from batalhas_repositorio import BatalhasRepositorio

DB_NOME = "pokemons.db"

repositorio_pokemons = PokemonsRepositorio(DB_NOME)
repositorio_batalha = BatalhasRepositorio(DB_NOME)
batalha = Batalha()
fase_jogo = 0
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
                if pokemon2.verificar_vida():
                    fase_jogo += 1
                    print(f"Vitória do {pokemon1.nome}")
                    repositorio_batalha.inserir_batalha(pokemon1, pokemon2)
                    
            else:
                pokemon2.ataque_aleatorio(pokemon1)
                if pokemon1.verificar_vida():
                    fase_jogo += 1
                    print(f"Vitória do {pokemon2.nome}")
                    repositorio_batalha.inserir_batalha(pokemon2, pokemon1)

        
                    
        case _:
            break