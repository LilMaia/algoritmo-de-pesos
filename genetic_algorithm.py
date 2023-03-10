import numpy as np
from scipy.spatial.distance import pdist, squareform

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
            #env.render()
            episode_reward += reward
        fitness_list.append(episode_reward)
    return fitness_list
    
def select_elite(pop_weights, fitness_list, pop_size):
    """
    Seleciona os membros mais aptos da população, com base na lista de pontuação.
    Retorna os pesos dos membros mais aptos.
    """
    elite_index = np.argsort(fitness_list)[::-1][:int(pop_size/2)] # Seleciona os índices dos membros mais aptos
    elite_weights = [pop_weights[i] for i in elite_index] # Obtém os pesos dos membros mais aptos
    elite_weights = np.vstack(elite_weights) # Empilha os pesos dos membros mais aptos em um array 2D
    return elite_weights
    
def generate_new_population(elite_weights, mutation_rate, env):
    """
    Gera uma nova população a partir dos membros mais aptos, realizando mutação e cruzamento.
    Retorna os pesos dos membros da nova geração.
    """
    new_weights = []
    # Calcular a matriz de distância entre os pesos
    elite_weights_2d = np.reshape(elite_weights, (len(elite_weights), -1)) # Transforma os pesos em um array 2D
    dist_matrix = squareform(pdist(elite_weights_2d)) # Calcula a matriz de distância entre os membros mais aptos
    average_distance = np.mean(dist_matrix) # Calcula a média da matriz de distância
    diversity_threshold = 0.5 * average_distance # Define o limite de diversidade com base na média da matriz de distância
    for i, elite_weight in enumerate(elite_weights):
        # Verificar se o membro atual é muito semelhante a outro membro na população
        if np.any(dist_matrix[i, :i] < diversity_threshold):
            # Ignorar este membro se ele for muito semelhante a outro membro
            continue
        child = elite_weight + mutation_rate*np.random.randn(*env.observation_space.shape) # Realiza mutação e gera um novo membro
        if np.array_equal(child, elite_weight):
            new_weights.append(elite_weight)
        else:
            new_weights.append(child)
    return new_weights
