import retro
import numpy as np
from population_utils import save_population, load_population
from hyperparameters import pop_size, n_generations, mutation_rate
from genetic_algorithm import evaluate_fitness, select_elite, generate_new_population

def train(env, filename):
    """
    Treina a população no ambiente env, salvando os pesos em filename.
    """
    try:
        pop_weights = load_population(filename)
        print(f"Loaded population from {filename}")
    except FileNotFoundError:
        pop_weights = [np.random.randn(*env.observation_space.shape) for _ in range(pop_size)]
        print(f"File {filename} not found. Initialized new population.")

    for i_generation in range(n_generations):
        print(f"Starting generation {i_generation}")
        try:
            fitness_list = evaluate_fitness(env, pop_weights)
            elite_weights = select_elite(pop_weights, fitness_list)
            new_weights = generate_new_population(elite_weights, mutation_rate, env)
            pop_weights = new_weights

            max_fitness = np.max(fitness_list)
            print(f'Generation {i_generation}: Max Fitness = {max_fitness}')

            save_population(pop_weights, filename)
            print(f"Population saved in {filename} at generation {i_generation}.")

        except KeyboardInterrupt:
            save_population(pop_weights, filename)
            print(f"Population saved in {filename} at generation {i_generation}.")
            break

if __name__ == '__main__':
    env = retro.make(game='DaffyDuckTheMarvinMissions-Snes')
    filename = 'population.npz'
    while True:
        print("1. Test current generation\n2. Continue evolution\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            pop_weights = load_population(filename)
            try:
                fitness_list = evaluate_fitness(env, pop_weights)
            except KeyboardInterrupt:
                break
            max_fitness = np.max(fitness_list)
            print(f'Max Fitness = {max_fitness}')
        elif choice == '2':
            train(env, filename)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
