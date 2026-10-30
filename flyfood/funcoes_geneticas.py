from deap import base,tools
import random
import lerflyfood

def invert(rota,quantidade,chance = 0.005):
    caminho = rota.copy()
    if random.random() < chance:
    
        for i in range(0,quantidade): 
        
            caminho = tools.mutInversion(caminho)[0]
        while caminho == rota:
            caminho = tools.mutInversion(caminho)[0]

        return caminho
    else:
        return rota.copy()

    
def swap(rota,quantidade,chance = 0.005):
    caminho = rota.copy()
    if random.random() < chance:
        for i in range(0,quantidade):
            indice1 = random.randint(0, len(rota) - 1)
            while True:
                indice2 = random.randint(0, len(rota) - 1)
                if indice1 != indice2:
                    break
            caminho[indice1], caminho[indice2] = caminho[indice2], caminho[indice1]
        while caminho == rota:
            indice1 = random.randint(0, len(rota) - 1)
            while True:
                indice2 = random.randint(0, len(rota) - 1)
                if indice1 != indice2:
                    break
            caminho[indice1], caminho[indice2] = caminho[indice2], caminho[indice1]
        return caminho
    else:
        return rota.copy()
    
def insert(rota,quantidade,chance = 0.005):
    caminho = rota.copy()
    if random.random() < chance:
    
        for i in range(0,quantidade): 
            indice1 = random.randint(0, len(rota) - 1)
            while True:
                indice2 = random.randint(0, len(rota) - 1)
                if indice1 != indice2:
                    break
            temp = caminho[indice1]
            if indice1 < indice2:
                for j in range(indice1,indice2):
                    caminho[j] = caminho[j+1]
                caminho[indice2] = temp
            else:
                for j in range(indice1,indice2,-1):
                    caminho[j] = caminho[j-1]
                caminho[indice2] = temp
        while caminho == rota:
            indice1 = random.randint(0, len(rota) - 1)
            while True:
                indice2 = random.randint(0, len(rota) - 1)
                if indice1 != indice2:
                    break
            temp = caminho[indice1]
            if indice1 < indice2:
                for j in range(indice1,indice2):
                    caminho[j] = caminho[j+1]
                caminho[indice2] = temp
            else:
                for j in range(indice1,indice2,-1):
                    caminho[j] = caminho[j-1]
                caminho[indice2] = temp
        return caminho
    else:
        return rota.copy()

def cruzamento(pai1,pai2,chance = 0.8):

    if random.random() < chance:
        # Converte as cidades de 1–58 para 0–57
        pai1copy = [cidade - 1 for cidade in pai1]
        pai2copy = [cidade - 1 for cidade in pai2]

        filho1, filho2 = tools.cxOrdered(pai1copy, pai2copy)

        # Volta para as cidades de 1–58
        filho1 = [cidade + 1 for cidade in filho1]
        filho2 = [cidade + 1 for cidade in filho2]

        return filho1, filho2

    else:
        return pai1.copy(), pai2.copy()

def opt2(individuos,dictDistancias,tentativas = 50):
    melhores_individuos = []
    melhores_aptidoes = []

    
    for individuo in individuos:
        individuo_atual = individuo.copy()
        aptidao_atual = lerflyfood.calculaAptidao([individuo_atual],dictDistancias)[0]
        for i in range(tentativas):
            novo_individuo = invert(individuo_atual,1,1)
            nova_aptidao = lerflyfood.calculaAptidao([novo_individuo],dictDistancias)[0]
            if  nova_aptidao < aptidao_atual:
                individuo_atual = novo_individuo
                aptidao_atual = nova_aptidao
            
        melhores_individuos.append(individuo_atual)
        melhores_aptidoes.append(aptidao_atual)
    
    return melhores_aptidoes, melhores_individuos