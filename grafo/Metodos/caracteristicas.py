'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np



'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

def tipoGrafo(matriz):
    dia = np.matrix(matriz)

    if np.where(matriz >= 2): #Significa que tem paralela
        if dia.diagonal().any == 1:  #Significa que tem laço
            print('É um pseudografo\n')
            return 3    #é peseudografo

        else: #Não tem laço
            print('É um multigrafo\n')
            return 2    #é multigrafo

    else:   #Não tem paralela
        if dia.diagonal().any == 0: #Não tem laço
            print('É um grafo simples\n')
            return 0

        else:
            print('É um digrafo\n')
            return 1

def calcDensidade(matriz):
    dia = np.matrix(matriz)
    if dia.diagonal().any == 0:  # Preciso saber se é digrafo ou não, por isso verei se tem loop
        Sum = 0
        nos = 0
        den = 0
        for i in range(len(matriz)):     #Pegando total de arestas
            Sum += len(matriz[i])

        nos = sum(map(sum, matriz)) #Pegando total de Nós
        den = (2*Sum) / nos * (nos-1)
        print('A densidade é: ' + "%.4f" % den + "\n")
        return ("%.4f" % den)

    else:                           #É digrafo, ja que tem loop
        Sum = 0
        nos = 0
        den = 0
        for i in range(len(matriz)):     #Pegando total de arestas
            Sum += len(matriz[i])

        nos = sum(map(sum, matriz)) #Pegando total de Nós
        den = Sum / nos * (nos-1)
        print('A densidade é: ' + "%.4f" % den + "\n")
        return ("%.4f" % den)

def insereAresta(matriz, vi, vj):

    # Adiciona as arestas
    print("Arestas Adicionadas em:{} {}\n".format(vi, vj))
    matriz[vj][vi] = 1
    matriz[vi][vj] = 1

    return np.array(np.array(matriz))

def removeAresta(matriz, vi, vj):

    # Removendo a aresta
    print("Arestas Removidas em: {} {}\n".format(vi, vj))
    matriz[vj][vi] = 0
    matriz[vi][vj] = 0

    return np.array(np.array(matriz))

def insereVertice(matriz, vi):
    print("Vertice Adicionado em: {} \n". format(vi))
    matriz[vi] = 1  #Simplesmente tornamos 1 a posição
    return np.array(np.array(matriz))

def removeVertice(matriz, vi):
    print("Vertice Removido em: {} \n".format(vi))
    matriz[vi] = 0   #Simplesmente removemos 1 da posição
    return np.array(np.array(matriz))
