def cria_tabuleiro(tamanho):
    '''Função que cria uma matriz formada por '-'s em todas as posições.
        Parâmetros:
            tamanho === tamanho do tabuleiro
    '''
    matriz = []
    for i in range(tamanho):
        matriz.append([])
        for j in range(tamanho):
            matriz[i].append('-')
    return matriz

def torre(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para a torre no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    for i in range(-tamanho, tamanho):
        if tamanho - linha + i >= 0 and coluna - 1 >= 0:
            if tamanho - linha + i < tamanho and coluna - 1 < tamanho:
                tabuleiro[tamanho - linha + i][coluna - 1] = 'x'
    for j in range(-tamanho, tamanho):
        if tamanho - linha >= 0 and coluna + j >= 0:
            if tamanho - linha < tamanho and coluna + j < tamanho:
                tabuleiro[tamanho - linha][coluna + j] = 'x'

def bispo(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para o bispo no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    for i in range(tamanho):
        if tamanho - linha + i >=0 and coluna - 1 + i >= 0:
            if tamanho - linha + i < tamanho and coluna - 1 + i < tamanho:
                tabuleiro[tamanho - linha + i ][coluna - 1 + i] = 'x'
        if tamanho - linha - i >=0 and coluna - 1 - i >= 0:
            if tamanho - linha - i < tamanho and coluna - 1 - i < tamanho:
                tabuleiro[tamanho - linha - i ][coluna - 1 - i] = 'x'
        if tamanho - linha + i >=0 and coluna - 1 - i >= 0: 
            if tamanho - linha + i < tamanho and coluna - 1 - i < tamanho:
                tabuleiro[tamanho - linha + i ][coluna - 1 - i] = 'x'
        if tamanho - linha - i >=0 and coluna - 1 + i >= 0:
            if tamanho - linha - i < tamanho and coluna - 1 + i < tamanho:
                tabuleiro[tamanho - linha - i ][coluna - 1 + i] = 'x'

def dama(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para a dama no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    torre(linha, coluna, tabuleiro, tamanho)
    bispo(linha, coluna, tabuleiro, tamanho)

def rei(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para o rei no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    for i in range(2):
        if tamanho - linha + i >=0 and coluna - 1 + i >= 0:
            if tamanho - linha + i < tamanho and coluna - 1 + i < tamanho:
                tabuleiro[tamanho - linha + i ][coluna - 1 + i] = 'x'
        if tamanho - linha - i >=0 and coluna - 1 - i >= 0:
            if tamanho - linha - i < tamanho and coluna - 1 - i < tamanho:
                tabuleiro[tamanho - linha - i ][coluna - 1 - i] = 'x'
        if tamanho - linha + i >=0 and coluna - 1 - i >= 0: 
            if tamanho - linha + i < tamanho and coluna - 1 - i < tamanho:
                tabuleiro[tamanho - linha + i ][coluna - 1 - i] = 'x'
        if tamanho - linha - i >=0 and coluna - 1 + i >= 0:
            if tamanho - linha - i < tamanho and coluna - 1 + i < tamanho:
                tabuleiro[tamanho - linha - i ][coluna - 1 + i] = 'x'
        if tamanho - linha + i  >= 0 and coluna - 1 >= 0:
            if tamanho - linha + i < tamanho and coluna - 1 < tamanho:
                tabuleiro[tamanho - linha + i ][coluna - 1] = 'x'
        if tamanho - linha - i >= 0 and coluna - 1 >= 0:
            if tamanho - linha - i < tamanho and coluna - 1 < tamanho:
                tabuleiro[tamanho - linha - i ][coluna - 1] = 'x'

    for j in range(2):
        if tamanho - linha >= 0 and coluna + j -1 >= 0:
            if tamanho - linha < tamanho and coluna + j - 1 < tamanho:
                tabuleiro[tamanho - linha][coluna + j - 1] = 'x'
        if tamanho - linha >= 0 and coluna -j - 1>= 0:
            if tamanho - linha < tamanho and coluna - j - 1 < tamanho:
                tabuleiro[tamanho - linha][coluna - j - 1] = 'x'


def cavalo(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para o cavalo no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    for i in [-1, 1]:
        for j in [-2, 2]:
            if tamanho - linha + i >= 0 and coluna + j - 1 >= 0:
                if tamanho - linha + i < tamanho and coluna + j - 1 < tamanho:
                    tabuleiro[tamanho - linha + i][coluna + j - 1] = 'x'
    for i in [-2, 2]:
            for j in [-1, 1]:
                if tamanho - linha + i >= 0 and coluna + j - 1 >= 0:
                    if tamanho - linha + i < tamanho and coluna + j - 1 < tamanho:
                        tabuleiro[tamanho - linha + i][coluna + j - 1] = 'x'


def peao(linha, coluna, tabuleiro, tamanho):
    ''' Função que grava os movimentos possíveis para o peão no tabuleiro.
    Parâmetros:
        linha === linha em que a peça está localizada
        coluna === coluna em que a peça está localizada
        tabuleiro === matriz-tabuleiro em que os movimentos serão marcados
        tamanho === tamanho do tabuleiro
    '''
    if linha == 2:
        if tamanho - linha - 2 >= 0 and coluna - 1 >= 0:
            if tamanho - linha - 2 < tamanho and coluna - 1 < tamanho:
                tabuleiro[tamanho - linha - 2][coluna - 1] = 'x'
    if tamanho - linha - 1 >= 0 and coluna - 1 >= 0:
        if tamanho - linha - 1 < tamanho and coluna - 1 < tamanho:
            tabuleiro[tamanho - linha - 1][coluna - 1] = 'x'

def main():
    ''' Função principal do programa, responsável por receber as entradas, chamar outras funções e fornecer/imprimir os resultados pedidos
    Parâmetros:
        Sem parâmetros
    '''
    lista_tabuleiros = []
    lista_frases = []

    while True:
        tamanho_tabuleiro = int(input())
        if tamanho_tabuleiro != 0:
            peca_posicao = input().split(' ')
            peca = peca_posicao[0]
            linha = int(peca_posicao[2])
            coluna = ord(peca_posicao[1]) - 96
            lista_frases.append(f'Movimentos para a peca {peca} a partir da casa {peca_posicao[1]}{linha}.')
            tabuleiro = cria_tabuleiro(tamanho_tabuleiro)
            if peca == 'Torre':
                torre(linha, coluna, tabuleiro, tamanho_tabuleiro)
            if peca == 'Cavalo':
                cavalo(linha, coluna, tabuleiro, tamanho_tabuleiro)
            if peca == 'Peao':
                peao(linha, coluna, tabuleiro, tamanho_tabuleiro)
            if peca == 'Dama':
                dama(linha, coluna, tabuleiro, tamanho_tabuleiro)
            if peca == 'Rei':
                rei(linha, coluna, tabuleiro, tamanho_tabuleiro)
            if peca == 'Bispo':
                bispo(linha, coluna, tabuleiro, tamanho_tabuleiro)
            tabuleiro[tamanho_tabuleiro - linha][coluna - 1] = 'o'
            lista_tabuleiros.append(tabuleiro)
        else:
            break

    for i in range(len(lista_tabuleiros)):
        tabuleiro = lista_tabuleiros[i]
        tamanho_tabuleiro = len(lista_tabuleiros[i])
        print(lista_frases[i])
        for i in range(tamanho_tabuleiro):
            print(tamanho_tabuleiro - i, end= ' ')
            for j in range(tamanho_tabuleiro):
                print(tabuleiro[i][j], end=' ')
            print()
        print(' ', end = ' ')
        for i in [chr(i) for i in range(97, 97 + tamanho_tabuleiro)]:   
            print(i, end = ' ')
        print()
        print()


main()