import numpy as np
from population_utils import save_population, load_population
from genetic_algorithm import evaluate_fitness, select_elite, generate_new_population
from plotting_utils import plota_pontuaçao

def treino(env, filename, pop_size, n_generations, mutation_rate):
    """
    Treina a população no ambiente env, salvando os pesos em filename.
    """
    try:
        # Tenta carregar a população do arquivo
        pop_weights = load_population(filename)
        print(f"População carregada de {filename}")
    except FileNotFoundError:
        # Se o arquivo não existe, cria uma nova população aleatória
        pop_weights = [np.random.randn(*env.observation_space.shape) for _ in range(pop_size)]
        print(f"Arquivo {filename} não encontrado. Iniciando uma nova população.")

    # Inicia as listas para armazenar as pontuações máximas e médias de cada geração
    max_scores = []
    avg_scores = []

    # Loop pelas gerações
    for i_generation in range(n_generations):
        print(f"Começando a geração {i_generation}")
        try:
            # Avalia o fitness de cada indivíduo na população
            fitness_list = evaluate_fitness(env, pop_weights)
            # Seleciona os indivíduos mais aptos
            elite_weights = select_elite(pop_weights, fitness_list, pop_size)
            # Gera uma nova população a partir dos indivíduos selecionados
            new_weights = generate_new_population(elite_weights, mutation_rate, env)
            # Substitui a população anterior pela nova população
            pop_weights = new_weights

            # Calcula e armazena as pontuações máxima e média da geração
            max_fitness = np.max(fitness_list)
            avg_fitness = np.mean(fitness_list)
            max_scores.append(max_fitness)
            avg_scores.append(avg_fitness)

            # Imprime a pontuação máxima da geração atual
            print(f'Geração {i_generation}: Max Fitness = {max_fitness}')

            # Salva a população atual no arquivo
            save_population(pop_weights, filename)
            print(f"População salva em {filename} na geração {i_generation}.")

        except KeyboardInterrupt:
            # Se o usuário interromper a execução, salva a população atual no arquivo
            save_population(pop_weights, filename)
            print(f"População salva em {filename} na geração {i_generation}.")
            break

    # Plota as pontuações máximas e médias de cada geração
    plota_pontuaçao(max_scores, avg_scores)
