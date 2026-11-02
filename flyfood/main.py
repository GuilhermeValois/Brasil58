import lerflyfood as lerflyfood
import funcoes_controle as funcoes_controle
import time

#Parâmetros:
caso = 5
lerflyfood.escolhendo_caso(caso)  # Escolha o caso desejado (1, 2, 3, etc.)
tamanho_populacao = 100
tamanho_individuo = 9+caso
populacao = lerflyfood.inicializaPopulacao(tamanho_populacao, tamanho_individuo)
operador_mut_random = ["invert", "insert"] # escolha 2 mutações por vez, operador de mutação pode ser "invert", "insert" ou "swap"
porcentagem_distr_mut = 0.8
quantidade_mutacoes = 1
chance_mutacao = 0.01
chance_cruzamento = 0.8
selecao_torneio = 2
geracoes = 1000
#Para o SteadyState:
geracao_de_individuos = 100000#Total de indivíduos gerados = geracao_de_individuos * 2 (pois a cada geração são gerados 2 indivíduos) 


#Mutação randomizada por porcentagem

print("Iniciando algoritmo genético com abordagem geracional...")
populacaocopy = populacao.copy()
inicio = time.perf_counter()
rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaoGeracional(
    populacaocopy, 
    lerflyfood.distancias, 
    tamanho_populacao, 
    operador_mut_random,
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
print(f"Caminhos Equivalentes: {caminhos_equivalentes}")


#Abordagem com SteadyState

print("Iniciando algoritmo genético com abordagem SteadyState...")
populacaocopy = populacao.copy()
inicio = time.perf_counter()
rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaoSteadyState(
        populacaocopy, 
        lerflyfood.distancias, 
        operador_mut_random, 
        porcentagem_distr_mut,
        quantidade_mutacoes, 
        chance_mutacao, 
        chance_cruzamento,
        selecao_torneio, 
        geracao_de_individuos
    )
fim = time.perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo} segundos")
print("Melhor rota encontrada:", rota)
print(aptidao)
#se não quiser os caminhos equivalentes comente a linha abaixo:
print(f"Caminhos Equivalentes: {caminhos_equivalentes}")


#Abordagem com steady-ready e busca local

print("Iniciando algoritmo genético com abordagem SteadyState e busca local...")
populacaocopy = populacao.copy()
inicio = time.perf_counter()
rota, aptidao, caminhos_equivalentes = funcoes_controle.novaGeracaoSteadyStatecomOpt(
        populacaocopy, 
        lerflyfood.distancias, 
        operador_mut_random, 
        porcentagem_distr_mut,
        quantidade_mutacoes, 
        chance_mutacao, 
        chance_cruzamento,
        selecao_torneio, 
        geracao_de_individuos
    )
fim = time.perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo} segundos")
print("Melhor rota encontrada:", rota)
print(aptidao)
#se não quiser os caminhos equivalentes comente a linha abaixo:
print(f"Caminhos Equivalentes: {caminhos_equivalentes}")

    