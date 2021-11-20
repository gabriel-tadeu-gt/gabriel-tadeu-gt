def le_matriz_quadrada(ordem):
    ''' Função que lê uma matriz quadrada na sua representação usual, dada a sua ordem 
    e retorna tal matriz na forma de uma lista de listas 
        Parâmetro: ordem ---- indica a ordem da matriz que será lida
    '''
    matriz = []
    if ordem != 1:
        i = 0
        while i < ordem:
            matriz.append([])
            k = input()
            lista_numeros = k.split(' ')
            lista_numeros_inteiros = [int(k) for k in lista_numeros]
            matriz[i] = lista_numeros_inteiros
            i += 1
    else:
        k = int(input())
        matriz.append([k])
    return matriz


def ordem_menor_supermatriz_comum(matriz1, matriz2):
    ''' Função que encontra a ordem da menor supermatriz comum entre duas matrizes dadas.
    Faz isso encontrando primeiro a dimensão da maior submatriz comum entre elas.
        Parâmetros:
            matriz1 ---- Primeira matriz, na forma de uma lista de listas
            matriz2 ---- Segunda matriz, na forma de uma lista de listas
    '''
    ordem1, ordem2 = len(matriz1), len(matriz2)
    if ordem1 >= ordem2:
        maior, menor = ordem1, ordem2 #Ordem da maior e da menor matriz
        matriz_maior, matriz_menor = matriz1, matriz2 #A maior matriz e a menor matriz
    else:
        maior, menor = ordem2, ordem1 #Ordem da maior e da menor matriz
        matriz_maior, matriz_menor = matriz2, matriz1 #A maior matriz e a menor matriz
    
    primeiro_igual_borda = 0 #Variável para indicar que ainda não foi encontrado o elemento em comum procurado entre as matrizes
                             #Tal elemento é o comum entre um elemento da matriz maior e um das bordas da mariz menor   
    if primeiro_igual_borda == 0:
        for i in range(maior):
            for j in range(maior):
                for k in [0, menor - 1]:
                    for l in [0, menor - 1]:
                        if matriz_maior[i][j] == matriz_menor[k][l]:
                            primeira_linha_igual_maior, primeira_coluna_igual_maior = i, j
                            primeira_linha_igual_menor, primeira_coluna_igual_menor = k, l
                            primeiro_igual_borda = 1
                            break
    igual_i, igual_j = 1, 1
    
    x, z = primeira_linha_igual_maior, primeira_linha_igual_menor #Linha do primeiro elemento em comum em cada uma das matrizes, a maior e a menor
    for y in range(maior): #Percorrendo a linha x da matriz maior
        for w in range(menor): #Percorrendo a linha z da matriz menor
            if matriz_maior[x][y] == matriz_menor[z][w]: #Se os elementos correspondentes são iguais, aumenta-se uma unidade no número de colunas
                                                         #da maior submatriz comum às duas
                    igual_j += 1 #Quantidade de colunas na maior submatriz comum entre as duas
    
    x, z = primeira_coluna_igual_maior, primeira_coluna_igual_menor #Coluna do primeiro elemento em comum em cada uma das matrizes, a maior e a menor
    for y in range(maior): #Percorrendo a coluna x da matriz maior
        for w in range(menor): #Percorrendo a coluna y da matriz menor
            if matriz_maior[y][x] == matriz_menor[w][z]: #Se os elementos correspondentes são iguais, aumenta-se uma unidade no número de linhas
                                                         #da maior submatriz comum às duas
                igual_i += 1 #Quantidade de linhas na maior submatriz comum entre as duas
    #Sendo a supermatriz comum entre as duas matrizes de ordem x por y
    m, n = (ordem1 + ordem2 + 1 - igual_i), (ordem1 + ordem2 + 1 - igual_j) #Cálculo da ordem da menor supermatriz comum
    return f'{m} x {n}' 


def lista_de_ordens():
    ''' Função unificadora do programa, lê os inputs de dados sobre as ordens das matrizes a serem comparadas,
    determinando se deve continuar de acordo com eles e calcula a ordem da menor supermatriz comum entre as duas,
    armazenando tal resultado em uma lista que depois é impressa como saída do programa
        Sem parâmetros
    '''
    lista_ordens = []
    while True: #Loop de obtenção
        x = input()
        if x != '0 0':
            ordem1, ordem2 = int(x.split(' ')[0]), int(x.split(' ')[1])
            matriz1, matriz2 = le_matriz_quadrada(ordem1), le_matriz_quadrada(ordem2)
            lista_ordens.append(ordem_menor_supermatriz_comum(matriz1, matriz2))
        else:
            break
    i = 0
    while i in range(len(lista_ordens)): #Loop de impressão
        print(lista_ordens[i])
        i += 1

lista_de_ordens()


