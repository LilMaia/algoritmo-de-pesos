from population_utils import load_population
from genetic_algorithm import evaluate_fitness

def testar_geração(env, filename):
    pop_weights = load_population(filename)
    try:
        fitness_list = evaluate_fitness(env, pop_weights)
    except KeyboardInterrupt:
        return
    max_fitness = np.max(fitness_list)
    print(f'Max Fitness = {max_fitness}')