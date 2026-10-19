import lerflyfood as lerflyfood
import funcoes_controle as funcoes_controle
import time

#Parâmetros:
caso = 3
lerflyfood.escolhendo_caso(caso)  # Escolha o caso desejado (1, 2, 3, etc.)
tamanho_populacao = 100
tamanho_individuo = 8+caso
populacao = lerflyfood.inicializaPopulacao(tamanho_populacao, tamanho_individuo)
operador_mutacao = "insert"#Operador de mutação pode ser "invert", "insert" ou "swap"
quantidade_mutacoes = 1
chance_mutacao = 0.15
chance_cruzamento = 0.8
selecao_torneio = 3
geracoes = 1000

inicio = time.perf_counter()
rota, aptidao = funcoes_controle.novaGeracao(
    populacao, 
    lerflyfood.distancias, 
    tamanho_populacao, 
    operador_mutacao, 
    quantidade_mutacoes, 
    chance_mutacao, 
    chance_cruzamento,
    selecao_torneio, 
    geracoes
    )
fim = time.perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo} segundos")
print("Melhor rota encontrada:", rota)
print("Aptidão:", aptidao)

