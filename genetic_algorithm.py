import numpy as np
from hyperparameters import pop_size

def evaluate_fitness(env, pop_weights):
    """
    Avalia o desempenho de cada membro da população no ambiente env.
    Retorna uma lista com a pontuação de cada membro.
    """
    fitness_list = []
    for i_member, member_weights in enumerate(pop_weights):
        obs = env.reset()
        done = False
        episode_reward = 0
        while not done:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            env.render()
            episode_reward += reward
        fitness_list.append(episode_reward)
    return fitness_list
    
def select_elite(pop_weights, fitness_list):
    """
    Seleciona os membros mais aptos da população, com base na lista de pontuação.
    Retorna os pesos dos membros mais aptos.
    """
    elite_index = np.argsort(fitness_list)[::-1][:int(pop_size/2)]
    elite_weights = [pop_weights[i] for i in elite_index]
    elite_weights = np.vstack(elite_weights)
    return elite_weights
    
def generate_new_population(elite_weights, mutation_rate, env):
    """
    Gera uma nova população a partir dos membros mais aptos, realizando mutação e cruzamento.
    Retorna os pesos dos membros da nova geração.
    """
    new_weights = []
    for _ in range(pop_size):
        parent1, parent2 = np.random.choice(elite_weights, size=2, replace=False)
        child = parent1 + mutation_rate*np.random.randn(*env.observation_space.shape)
        new_weights.append(child)
    return new_weights