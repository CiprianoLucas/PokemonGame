## POKEMON GAME

É um projeto de aprendizagem de programação orientada a objetos. Seguindo os critérios

#### Objetivo:
Criar um jogo de batalha Pokémon baseado em turnos que funcione através do terminal. O jogo deve ser implementado em Python, utilizando os conceitos de Programação Orientada a Objetos (POO) e salvando os dados em um banco de dados.

#### Descrição do Jogo:
O jogo simula batalhas entre Pokémon, onde cada jogador escolhe um Pokémon e os comanda em uma batalha por turnos. Cada Pokémon possui diferentes habilidades, pontos de vida (HP) e status.

#### FUNCIONALIDADES PRINCIPAIS:
Seleção de Pokémon:
Permitir que os jogadores escolham um Pokémon de uma lista pré-definida.
Cada Pokémon terá atributos como nome, tipo, HP, ataques e defesas.

#### Batalha em Turnos:
Implementar um sistema de batalha baseado em turnos onde cada Pokémon pode realizar uma ação por vez (atacar, defender, usar item).
Implementar um sistema de vantagens e desvantagens baseado nos tipos dos Pokémon.

#### Sistema de HP e Status:
Cada Pokémon tem um HP que diminui com os ataques. Quando o HP chega a zero, o Pokémon é considerado desmaiado.
Implementar efeitos de status como envenenamento ou paralisia.

### Implementação com POO:
#### Classes:
- Pokemon: Representa um Pokémon, com atributos como nome, tipo, hp, ataques.
- Ataque: Representa um ataque, com atributos como nome, dano, tipo.
- Batalha: Gerencia a lógica da batalha, controlando os turnos e ações dos Pokémon.
- Banco de Dados:
Utilizar SQLite para armazenar informações dos Pokémon e dos jogadores.
Criar tabelas para Pokémon, Ataques, e registros de batalhas.
- Interface do Console:
Desenvolver uma interface de linha de comando para interação do usuário.
Implementar menus para seleção de Pokémon, visualização de status e escolha de ações durante a batalha.

### Instalando

Necessário ter Python 3 instalado.

Clone o repositório, abra o cmd na pasta raiz e execute
```cmd
python main.py
```

