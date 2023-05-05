from modelo_utils import gerar_ação
import random

def avaliar_aptidão(ambiente, pesos_da_população, modelo):

    print(f"-------------------------------------------------------------------------------------")
    print(f"população_utils:")
    #print(f"Pesos da população: {pesos_da_população}")
    
    # Inicia uma lista vazia para armazenar as pontuações dos membros da população
    lista_de_aptidão = []

    # Máximo de iterações que o While pode fazer
    máximo_de_iterações=7000
    
    # Itera sobre cada membro da população e avalia seu desempenho no ambiente
    for i_membro, pesos_do_membro in enumerate(pesos_da_população):
        
        # Reseta o ambiente para começar um novo episódio
        estado_atual_do_ambiente = ambiente.reset()
        
        # Inicia a variável que indica se o episódio terminou
        concluído = False
        
        # Inicia a variável que armazenará a recompensa total do episódio
        recompensa_do_episódio = 300000
        
        # Inicia o contador
        iterações = 0
        
        # Armazena a pontuação de cada iteração
        pontuação_atual = 0
        
        # Armazena a vida a cada iteração
        vida_atual = 0
        
        # Armazena a quantidade de vidas a cada iteração
        quantidade_de_vidas = 0
        
        # Enquanto o episódio não terminar e o número máximo de iterações não for atingido, executa a ação sugerida pela rede neural e coleta a recompensa
        while not concluído and iterações < máximo_de_iterações:
            
            # Gera uma ação para o estado atual do ambiente utilizando a rede neural e os pesos do membro atual com 90% de chance
            if random.random() < 0.9:
                #print(f"Ação pensada")
                ação = gerar_ação(estado_atual_do_ambiente, modelo, pesos=pesos_do_membro)
            else:
                #print(f"Ação aleatoria")
                ação = ambiente.action_space.sample()
            
            # Executa a ação no ambiente e recebe a observação do próximo estado, a recompensa e se o episódio terminou
            estado_atual_do_ambiente, recompensa, concluído, informações_adicionais = ambiente.step(ação)
            
            # Renderiza o ambiente (opcional, apenas para visualização)
            #ambiente.render()
            
            # Adiciona a recompensa do passo atual à recompensa total do episódio
            recompensa_do_episódio += recompensa
            
            # Incrementa a recompensa se o agente avançar na fase
            if informações_adicionais['score'] > pontuação_atual:
                recompensa_do_episódio += 100000
            elif informações_adicionais['score'] == 0:
                recompensa_do_episódio -= 100
            # elif informações_adicionais['score'] < pontuação_atual:
            #     recompensa_do_episódio -= 50000
            # elif informações_adicionais['score'] == pontuação_atual:
            #     recompensa_do_episódio += 10
                
            # Incrementa a recompensa de acordo com a barra de vida do personagem
            if informações_adicionais['health'] < vida_atual:
                recompensa_do_episódio -= 500
            # elif informações_adicionais['health'] > vida_atual: 
            #     recompensa_do_episódio += 20
            # elif informações_adicionais['health'] == vida_atual: 
            #     recompensa_do_episódio += 10
                
            # Incrementa a recompensa de acordo com a quantidade de vidas(tentativas) do personagem
            if informações_adicionais['lives'] < quantidade_de_vidas:
                recompensa_do_episódio -= 50000
            # elif informações_adicionais['lives'] > quantidade_de_vidas: 
            #     recompensa_do_episódio += 20
            # elif informações_adicionais['lives'] == quantidade_de_vidas: 
            #     recompensa_do_episódio += 10
            
            # Pegando a pontuação atual da iteração para usar de comparativo na proxima iteração
            pontuação_atual = informações_adicionais['score']
            
            # Pegando a vida atual da iteração para usar de comaprativo na proxima iteração
            vida_atual = informações_adicionais['health']
            
            # Pegando a quantidade de vidas que o agente possui a cada iteração
            quantidade_de_vidas = informações_adicionais['lives']
            
            # ação = ação = [random.randint(1, 100)]
            # estado_atual_do_ambiente, recompensa, concluído, informações_adicionais = ambiente.step(ação)
            
            # Incrementa o contador
            iterações += 1
        
        # Armazena a pontuação do membro atual na lista de pontuações da população
        print(f"Recompensa do episódio : {recompensa_do_episódio}")
        lista_de_aptidão.append(recompensa_do_episódio)
    
    # Retorna a lista de pontuações da população
    print(f"-------------------------------------------------------------------------------------")
    return lista_de_aptidão
