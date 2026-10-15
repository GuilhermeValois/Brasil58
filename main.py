import lerbrasil
import funcoes_controle
import time

#Parâmetros:
tamanho_população = 100
tamanho_individuo = 58
populacao = lerbrasil.inicializaPopulacao(tamanho_população, tamanho_individuo)
operador_mutação = "inversao"#Operador de mutação pode ser "inversao", "insert" ou "swap"
quantidade_mutacoes = 1
chance_mutacao = 0.01
chance_cruzamento = 0.8
geracoes = 300

inicio = time.perf_counter()
rota, aptidao = funcoes_controle.novaGeracao(
    populacao, 
    lerbrasil.distancias, 
    tamanho_população, 
    operador_mutação, 
    quantidade_mutacoes, 
    chance_mutacao, 
    chance_cruzamento, 
    geracoes
    )
fim = time.perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo} segundos")
print("Melhor rota encontrada:", rota)
print("Aptidão:", aptidao)

