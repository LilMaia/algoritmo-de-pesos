import retro
from treino import treino
from teste import testar_geração
from modelo import criar_modelo

# define os hiperparâmetros do algoritmo evolutivo
tamanho_da_população = 25
número_de_gerações = 1000
taxa_de_mutação = 0.05

if __name__ == '__main__':
    
    # Cria o ambiente do jogo
    ambiente = retro.make(game='DaffyDuckTheMarvinMissions-Snes')
    
    # Define o nome do arquivo para salvar a população
    nome_do_arquivo = 'população.npz'

    # Cria o modelo para avaliar as ações e/ou gerar os pesos iniciais
    modelo = criar_modelo(ambiente)
    
    while True:
        print("1. Continuar evolução\n2. Testar atual geração\n3. Sair")
        escolha = input("Digite sua escolha: ")
        if escolha == '1':
            treino(ambiente, nome_do_arquivo, tamanho_da_população, número_de_gerações, taxa_de_mutação, modelo)
        elif escolha == '2':
            testar_geração(ambiente, nome_do_arquivo, modelo)
        elif escolha == '3':
            break
        else:
            print("Escolha errada. Por favor, tente novamente.")