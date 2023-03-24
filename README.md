# TCC sobre Algoritmos Evolucionários em Jogos Retro
Este projeto implementa um algoritmo evolucionário em jogos retro usando a biblioteca retro. O objetivo do projeto é treinar uma população de agentes para jogar o jogo "DaffyDuckTheMarvinMissions-Snes" e obter a maior pontuação possível.

# Arquivos

train.py: este arquivo contém o código principal do projeto. Ele define a função train(), que treina a população no ambiente especificado, e a função main(), que permite ao usuário escolher entre testar a geração atual, continuar a evolução ou sair do programa.

population_utils.py: este arquivo contém as funções para salvar e carregar a população atual em um arquivo.

hyperparameters.py: este arquivo define os hiperparâmetros do algoritmo evolutivo, como tamanho da população, número de gerações e taxa de mutação.

genetic_algorithm.py: este arquivo contém as funções principais do algoritmo evolutivo, como avaliar o desempenho dos membros da população, selecionar os membros mais aptos e gerar uma nova população.

# Uso

Para executar o treinamento da população, execute o seguinte comando:

python main.py

O programa iniciará com um menu que permitirá ao usuário escolher entre testar a geração atual, continuar a evolução ou sair do programa.

Os pesos da população atual serão salvos em um arquivo chamado population.npz.

# Requisitos

Este projeto requer a biblioteca import retro e a biblioteca padrão do Python. Para instalar a biblioteca import retro, execute o seguinte comando:

pip install gym-retro
