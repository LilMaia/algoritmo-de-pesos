import random
from modelo_utils import gerar_ação

def avaliar_aptidão(ambiente, pesos_da_população, modelo):
    
    lista_de_aptidão = []

    máximo_de_iterações=4001
    
    # Itera sobre cada membro da população e avalia seu desempenho no ambiente
    for pesos_do_membro in pesos_da_população:
        
        estado_atual_do_ambiente = ambiente.reset()
        
        concluído = False
        
        recompensa_do_episódio = 300000
        
        iterações = 0
        
        pontuação_atual = 0
        vida_atual = 0
        quantidade_de_vidas = 0
        
        atualizar_pesos = True
        
        pontuação_inicial = 0
        vida_inicial = 0
        quantidade_de_vida_inicial = 0
        
        # Enquanto o episódio não terminar e o número máximo de iterações não for atingido, executa a ação sugerida pela rede neural e coleta a recompensa
        while not concluído and iterações < máximo_de_iterações:
            
            ação = gerar_ação(estado_atual_do_ambiente, modelo, pesos_do_membro, atualizar_pesos)
            
            atualizar_pesos = False
            
            # Executa a ação no ambiente e recebe a observação do próximo estado, a recompensa e se o episódio terminou
            estado_atual_do_ambiente, recompensa, concluído, informações_adicionais = ambiente.step(ação)
            
            # Renderiza o ambiente (opcional, apenas para visualização)
            ambiente.render()
            
            # Adiciona a recompensa do passo atual à recompensa total do episódio
            recompensa_do_episódio += recompensa
            
            # Incrementa a recompensa se o agente avançar na fase
            if informações_adicionais['score'] > pontuação_atual:
                recompensa_do_episódio += 100000
            elif informações_adicionais['score'] == 0:
                recompensa_do_episódio -= 100
                
            # Incrementa a recompensa de acordo com a barra de vida do personagem
            if informações_adicionais['health'] < vida_atual:
                recompensa_do_episódio -= 500
                
            # Incrementa a recompensa de acordo com a quantidade de vidas(tentativas) do personagem
            if informações_adicionais['lives'] < quantidade_de_vidas:
                recompensa_do_episódio -= 50000
             
            if iterações <= 1 or iterações % 1001 == 0:
                pontuação_inicial = informações_adicionais['score']
                vida_inicial = informações_adicionais['health']
                quantidade_de_vida_inicial = informações_adicionais['lives']

            if iterações % 1000 == 0:
                if pontuação_atual == pontuação_inicial and vida_atual == vida_inicial and quantidade_de_vidas == quantidade_de_vida_inicial:
                    recompensa_do_episódio -= 300000

            # Pegando a pontuação atual da iteração para usar de comparativo na proxima iteração
            pontuação_atual = informações_adicionais['score']
            
            # Pegando a vida atual da iteração para usar de comaprativo na proxima iteração
            vida_atual = informações_adicionais['health']
            
            # Pegando a quantidade de vidas que o agente possui a cada iteração
            quantidade_de_vidas = informações_adicionais['lives']
            
            # Incrementa o contador
            iterações += 1
        
        # Armazena a pontuação do membro atual na lista de pontuações da população
        print(f"Recompensa do episódio : {recompensa_do_episódio}")
        lista_de_aptidão.append(recompensa_do_episódio)
    
    return lista_de_aptidão