from modelo_utils import gerar_ação

"""
    A função avaliar_aptidão avalia o desempenho de cada membro da população em um 
    determinado ambiente, utilizando uma rede neural para gerar a ação. Ela recebe 
    como entrada três parâmetros: o ambiente a ser avaliado, uma lista de pesos da 
    população (que serão utilizados pela rede neural para gerar a ação), 
    e o modelo da rede neural.

    A função itera sobre cada membro da população e avalia seu desempenho no ambiente,
    executando um novo episódio a cada iteração. Dentro de cada episódio, a função
    utiliza a rede neural e os pesos do membro atual para gerar uma ação para o estado
    atual do ambiente. Em seguida, a função executa a ação no ambiente, coleta a recompensa
    do passo atual e verifica se o episódio terminou. O episódio termina quando a variável
    concluído é definida como True.
    
    Se o episódio não terminar depois de determinada quantidade de iterações
    (definida na variável máximo_de_iterações),
    o loop é encerrado automaticamente. Além disso, a função armazena a pontuação do membro
    atual na lista de pontuações da população e retorna essa lista no final da execução.
"""

def avaliar_aptidão(ambiente, pesos_da_população, modelo):

    print(f"-------------------------------------------------------------------------------------")
    print(f"população_utils:")
    
    # Inicia uma lista vazia para armazenar as pontuações dos membros da população
    lista_de_aptidão = []

    # Máximo de iterações que o While pode fazer
    máximo_de_iterações=3000
    
    # Itera sobre cada membro da população e avalia seu desempenho no ambiente
    for i_membro, pesos_do_membro in enumerate(pesos_da_população):
        
        # Reseta o ambiente para começar um novo episódio
        estado_atual_do_ambiente = ambiente.reset()
        
        # Inicia a variável que indica se o episódio terminou
        concluído = False
        
        # Inicia a variável que armazenará a recompensa total do episódio
        recompensa_do_episódio = 1000
        
        # Inicia o contador
        iterações = 0
        
        # Enquanto o episódio não terminar e o número máximo de iterações não for atingido, executa a ação sugerida pela rede neural e coleta a recompensa
        while not concluído and iterações < máximo_de_iterações:
            
            # Gera uma ação para o estado atual do ambiente utilizando a rede neural e os pesos do membro atual
            ação = gerar_ação(estado_atual_do_ambiente, modelo, pesos=pesos_do_membro)
            
            # Executa a ação no ambiente e recebe a observação do próximo estado, a recompensa e se o episódio terminou
            estado_atual_do_ambiente, recompensa, concluído, informações_adicionais = ambiente.step(ação)
            
            # Renderiza o ambiente (opcional, apenas para visualização)
            ambiente.render()
            
            # Adiciona a recompensa do passo atual à recompensa total do episódio
            recompensa_do_episódio += recompensa
            
            # Incrementa o contador
            iterações += 1
        
        # Armazena a pontuação do membro atual na lista de pontuações da população
        print(f"Recompensa do episódio : {recompensa_do_episódio}")
        lista_de_aptidão.append(recompensa_do_episódio)
    
    # Retorna a lista de pontuações da população
    print(f"-------------------------------------------------------------------------------------")
    return lista_de_aptidão
