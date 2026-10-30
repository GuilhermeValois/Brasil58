import lerflyfood as lerflyfood
import random
import funcoes_geneticas as funcoes_geneticas
import lerflyfood

def menor(nova_populacao,aptidoes):

    caminhos_equivalentes = []
    menor_indice = min(range(len(nova_populacao)), key = lambda i: aptidoes[i])
    for i in range(len(nova_populacao)):
        if nova_populacao[i] == nova_populacao[menor_indice] and i != menor_indice:
            caminhos_equivalentes.append(nova_populacao[i])
    return nova_populacao[menor_indice], aptidoes[menor_indice], caminhos_equivalentes

def selecaotorneio(populacao, aptidoes, k):
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


        listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)

        menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais = menor(populacao, listaAptidao)

        nova_populacao = []

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

        aptidoes = lerflyfood.calculaAptidao(nova_populacao, dicDistancias)
        menor_individuo_atual, menor_aptidao_atual, caminhos_equivalentes = menor(nova_populacao, aptidoes)
        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
            caminhos_equivalentes_globais = caminhos_equivalentes
        populacao = nova_populacao
        
    
    return menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais


def novaGeracaoPorcento(
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

    listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)
    menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais = menor(populacao, listaAptidao)
    for geracao in range(geracoes):

        listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)
        nova_populacao = []
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

        aptidoes = lerflyfood.calculaAptidao(nova_populacao, dicDistancias)
        menor_individuo_atual, menor_aptidao_atual, caminhos_equivalentes = menor(nova_populacao, aptidoes)
        
        populacao = nova_populacao

        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
            caminhos_equivalentes_globais = caminhos_equivalentes
        
    return menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais

def novaGeracaoPorcentocomDiversificacao(
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
    contador = 0
    geracao_marco = 0
    selecao_atual = selecao_torneio
    mutaca_chance_atual = chanceMutacao
    listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)
    menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais = menor(populacao, listaAptidao)
    aptidao_anterior = menor_aptidao_global
    for geracao in range(geracoes):

        listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)
        nova_populacao = []
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

        aptidoes = lerflyfood.calculaAptidao(nova_populacao, dicDistancias)
        menor_individuo_atual, menor_aptidao_atual, caminhos_equivalentes = menor(nova_populacao, aptidoes)

        if aptidao_anterior == menor_aptidao_atual:
            contador += 1
        else:
            aptidao_anterior = menor_aptidao_atual
            contador = 0
        if contador >= 25:
            contador = 0
            selecao_torneio = 2
            if chanceMutacao+0.15<1:
                chanceMutacao += 0.15
            else:
                chanceMutacao = 1
            geracao_marco = geracao
        if (geracao - geracao_marco) == 20:
            chanceMutacao =  mutaca_chance_atual
            selecao_torneio = selecao_atual
        
        populacao = nova_populacao

        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
            caminhos_equivalentes_globais = caminhos_equivalentes
        
    return menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais


def novaGeracaosteadyready(
    populacao,
    dicDistancias,
    operadorMutradom=["invert","insert"],
    porcentagem = 0.5,
    quantidadeMutacoes=1,
    chanceMutacao=0.01,
    chanceCruzamento=0.8,
    selecao_torneio=3,
    geracoes = 10
):
    contador_estagnacao = 0
    houve_melhoria = False
    listaAptidao = lerflyfood.calculaAptidao(populacao, dicDistancias)
    menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais = menor(populacao, listaAptidao)
    for _ in range(geracoes):

        novos_individuos = []

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

        novos_individuos.append(filho1)
        novos_individuos.append(filho2)

        aptidoes = lerflyfood.calculaAptidao(novos_individuos, dicDistancias)

        for aptidao in aptidoes:
            listaAptidao.append(aptidao)

        populacao.append(filho1)
        populacao.append(filho2)

        maior_indice = max(range(len(populacao)), key = lambda i: listaAptidao[i])
        populacao.pop(maior_indice)
        listaAptidao.pop(maior_indice)
        maior_indice = max(range(len(populacao)), key = lambda i: listaAptidao[i])
        populacao.pop(maior_indice)
        listaAptidao.pop(maior_indice)
        
        menor_individuo_atual, menor_aptidao_atual, caminhos_equivalentes = menor(populacao, listaAptidao)

        if menor_aptidao_atual < menor_aptidao_global:
            houve_melhoria = True
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
        else:
            houve_melhoria = False

        if houve_melhoria:
            contador_estagnacao = 0
        else:
            contador_estagnacao += 1

        if contador_estagnacao >= 20:
            melhores_individuos = []
            
            for i in range(20):
                menor_indice = min(range(len(populacao)), key = lambda i: listaAptidao[i])
                melhores_individuos.append(populacao[menor_indice])
                populacao.pop(menor_indice)
                listaAptidao.pop(menor_indice)
            novas_aptidoes, individuos = funcoes_geneticas.opt2(melhores_individuos,dicDistancias)
            for i in range(len(individuos)):
                populacao.append(individuos[i])
                listaAptidao.append(novas_aptidoes[i])

            menor_individuo_atual, menor_aptidao_atual, caminhos_equivalentes = menor(populacao, listaAptidao)

            contador_estagnacao = 0
                #print(f"Menor individuo atual da geracao {_}: {menor_aptidao_atual}")
        if menor_aptidao_atual < menor_aptidao_global:
            menor_individuo_global = menor_individuo_atual
            menor_aptidao_global = menor_aptidao_atual
            caminhos_equivalentes_globais = caminhos_equivalentes

    return menor_individuo_global, menor_aptidao_global, caminhos_equivalentes_globais
