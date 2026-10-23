import lerbrasil as lerbrasil
import random
import funcoes_geneticas as funcoes_geneticas

def menor(nova_populacao,aptidoes):

    menor_indice = min(range(len(nova_populacao)), key = lambda i: aptidoes[i])
    return nova_populacao[menor_indice], aptidoes[menor_indice]

def selecaotorneio(populacao, aptidoes,k):
    candidatos = random.sample(range(len(populacao)),min(k,len(populacao)))
    melhor_candiato = min(candidatos, key = lambda i: aptidoes[i])
    return melhor_candiato

def novaGeracao(
    populacao,
    dicDistancias,
    tamanhoPop,
    operadorMutacao="inversao",
    quantidadeMutacoes=1,
    chanceMutacao=0.01,
    chanceCruzamento=0.8,
    selecao_torneio=3,
    geracoes = 10
):
    for _ in range(geracoes):


        listaAptidao = lerbrasil.calculaAptidao(populacao, dicDistancias)

        menor_individuo_global, menor_aptidao_global = menor(populacao, listaAptidao)

        pai1 = populacao[selecaotorneio(populacao, listaAptidao, selecao_torneio)]
        pai2 = populacao[selecaotorneio(populacao, listaAptidao, selecao_torneio)]

        filho1, filho2 =funcoes_geneticas.cruzamento(pai1, pai2, chanceCruzamento)

        if operadorMutacao == "invert":
            filho1 = funcoes_geneticas.invert(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.invert(filho2, quantidadeMutacoes, chanceMutacao)
        elif operadorMutacao == "insert":
            filho1 = funcoes_geneticas.insert(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.insert(filho2, quantidadeMutacoes, chanceMutacao)
        else:
            filho1 = funcoes_geneticas.swap(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.swap(filho2, quantidadeMutacoes, chanceMutacao)

        nova_populacao = [filho1, filho2]

        while len(nova_populacao) < tamanhoPop:
            pai1 = populacao[selecaotorneio(populacao, listaAptidao,selecao_torneio)]
            pai2 = populacao[selecaotorneio(populacao, listaAptidao,selecao_torneio)]

            filho1, filho2 = funcoes_geneticas.cruzamento(pai1, pai2, chanceCruzamento)

            if operadorMutacao == "invert":
                filho1 = funcoes_geneticas.invert(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.invert(filho2, quantidadeMutacoes, chanceMutacao)
            elif operadorMutacao == "insert":
                filho1 = funcoes_geneticas.insert(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.insert(filho2, quantidadeMutacoes, chanceMutacao)
            else:
                filho1 = funcoes_geneticas.swap(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.swap(filho2, quantidadeMutacoes, chanceMutacao)
        
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        aptidoes = lerbrasil.calculaAptidao(nova_populacao, dicDistancias)
        menor_individuo_atual, menor_aptidao_atual = menor(nova_populacao, aptidoes)
        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
        populacao = nova_populacao
        
    
    return menor_individuo_global, menor_aptidao_global


def novaGeracaoporcento(
    populacao,
    dicDistancias,
    tamanhoPop,
    operadorMutradom=["invert","insert"],
    porcentagem = 0.5,
    quantidadeMutacoes=1,
    chanceMutacao=0.01,
    chanceCruzamento=0.8,
    selecao_torneio=3,
    geracoes = 10
):
    for geracao in range(geracoes):


        listaAptidao = lerbrasil.calculaAptidao(populacao, dicDistancias)

        menor_individuo_global, menor_aptidao_global = menor(populacao, listaAptidao)

        pai1 = populacao[selecaotorneio(populacao, listaAptidao, selecao_torneio)]
        pai2 = populacao[selecaotorneio(populacao, listaAptidao, selecao_torneio)]

        filho1, filho2 =funcoes_geneticas.cruzamento(pai1, pai2, chanceCruzamento)
        if random.random() > porcentagem:
            operadorMutacao = operadorMutradom[1]
        else:
            operadorMutacao = operadorMutradom[0]

        if  operadorMutacao == "invert":
            filho1 = funcoes_geneticas.invert(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.invert(filho2, quantidadeMutacoes, chanceMutacao)
        elif operadorMutacao == "insert":
            filho1 = funcoes_geneticas.insert(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.insert(filho2, quantidadeMutacoes, chanceMutacao)
        else:
            filho1 = funcoes_geneticas.swap(filho1, quantidadeMutacoes, chanceMutacao)
            filho2 = funcoes_geneticas.swap(filho2, quantidadeMutacoes, chanceMutacao)

        nova_populacao = [filho1, filho2]

        while len(nova_populacao) < tamanhoPop:
            pai1 = populacao[selecaotorneio(populacao, listaAptidao,selecao_torneio)]
            pai2 = populacao[selecaotorneio(populacao, listaAptidao,selecao_torneio)]

            filho1, filho2 = funcoes_geneticas.cruzamento(pai1, pai2, chanceCruzamento)

            if random.random() > porcentagem:
                operadorMutacao = operadorMutradom[1]
            else:
                operadorMutacao = operadorMutradom[0]

            if operadorMutacao == "invert":
                filho1 = funcoes_geneticas.invert(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.invert(filho2, quantidadeMutacoes, chanceMutacao)
            elif operadorMutacao == "insert":
                filho1 = funcoes_geneticas.insert(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.insert(filho2, quantidadeMutacoes, chanceMutacao)
            else:
                filho1 = funcoes_geneticas.swap(filho1, quantidadeMutacoes, chanceMutacao)
                filho2 = funcoes_geneticas.swap(filho2, quantidadeMutacoes, chanceMutacao)
        
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        aptidoes = lerbrasil.calculaAptidao(nova_populacao, dicDistancias)
        menor_individuo_atual, menor_aptidao_atual = menor(nova_populacao, aptidoes)
        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
        populacao = nova_populacao
        
    
    return menor_individuo_global, menor_aptidao_global