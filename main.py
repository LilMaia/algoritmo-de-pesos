# Imports do python
import retro
import numpy as np

# Imports dos outros arquivos
from training_utils import treino
from test_utils import testar_geração

if __name__ == '__main__':
    # Cria o ambiente do jogo
    env = retro.make(game='DaffyDuckTheMarvinMissions-Snes')
    # Define o nome do arquivo para salvar a população
    filename = 'population.npz'
    while True:
        print("1. Continuar evolução\n2. Testar atual geração\n3. Sair")
        choice = input("Digite sua escolha: ")
        if choice == '1':
            treino(env, filename)
        elif choice == '2':
            testar_geração(env, filename)
        elif choice == '3':
            break
        else:
            print("Escolha errada. Por favor, tente novamente.")
