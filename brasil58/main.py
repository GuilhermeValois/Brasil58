import lerbrasil as lerbrasil
import funcoes_controle as funcoes_controle
import time

#Parâmetros:
tamanho_populacao = 100
tamanho_individuo = 58
populacao = lerbrasil.inicializaPopulacao(tamanho_populacao, tamanho_individuo)
operador_mutacao = "invert"#Operador de mutação pode ser "invert", "insert" ou "swap"
operador_mutrandom = ["invert", "swap"] # escolha 2 mutações por vez
porcentagem_distr_mut = 0.8
quantidade_mutacoes = 1
chance_mutacao = 0.01
chance_cruzamento = 0.8
selecao_torneio = 7
geracoes = 1000

#Mutação selecionada
'''
for i in range(20):    
    inicio = time.perf_counter()
    rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracao(
        populacao, 
        lerbrasil.distancias, 
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
    print(aptidao)
    #se não quiser os caminhos equivalentes comente a linha abaixo:
    print(caminhos_equivalentes)
'''

#Mutação randomizada por porcentagem

for i in range(20):    
    inicio = time.perf_counter()
    rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaoporcento(
        populacao, 
        lerbrasil.distancias, 
        tamanho_populacao, 
        operador_mutrandom,
        porcentagem_distr_mut, 
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
    print(aptidao)
    #se não quiser os caminhos equivalentes comente a linha abaixo:
    print(caminhos_equivalentes)
   