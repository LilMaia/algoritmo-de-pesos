import matplotlib.pyplot as plt

def plota_pontuação(max_scores, avg_scores):
    """
    Plota as pontuações máximas e médias ao longo do tempo.
    """
    plt.plot(max_scores, label='Pontuação máxima')
    plt.plot(avg_scores, label='Pontuação média')
    plt.xlabel('Geração')
    plt.ylabel('Pontuação')
    plt.legend()
    plt.show()