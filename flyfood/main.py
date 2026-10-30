import lerflyfood as lerflyfood
import funcoes_controle as funcoes_controle
import time

#Parâmetros:
caso = 1
lerflyfood.escolhendo_caso(caso)  # Escolha o caso desejado (1, 2, 3, etc.)
tamanho_populacao = 100
tamanho_individuo = 9+caso
populacao = lerflyfood.inicializaPopulacao(tamanho_populacao, tamanho_individuo)
operador_mutacao = "insert"#Operador de mutação pode ser "invert", "insert" ou "swap"
operador_mutrandom = ["invert", "insert"] # escolha 2 mutações por vez
porcentagem_distr_mut = 0.8
quantidade_mutacoes = 1
chance_mutacao = 0.15
chance_cruzamento = 0.8
selecao_torneio = 3
geracoes = 1000

inicio = time.perf_counter()
rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracao(
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
#se não quiser os caminhos equivalentes comente a linha abaixo:
print(caminhos_equivalentes)

#Mutação randomizada por porcentagem

'''
for i in range(20):    
    inicio = time.perf_counter()
    rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaoPorcento(
        populacao, 
        lerflyfood.distancias, 
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
'''

#Abordagem com steady-ready e busca local

'''
print(f"chance de mutacao = {chance_mutacao}")
for i in range(20):
    
    populacaocopy = populacao.copy()
    inicio = time.perf_counter()
    rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaosteadyready(
        populacaocopy, 
        lerflyfood.distancias, 
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
    #print(f"Tempo de execução: {tempo} segundos")
    #print("Melhor rota encontrada:", rota)
    print(aptidao)
    #se não quiser os caminhos equivalentes comente a linha abaixo:
    #print(caminhos_equivalentes)
'''