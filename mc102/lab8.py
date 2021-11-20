def avaliar_algebra(lista):
    '''Avalia o valor de uma expressão puramente algébrica, sem nenhum tipo de comparação. É sempre executada primeiro para eliminar as 
    operações mais básicas e - nas comparações - trabalhar apenas com números. Retorna uma lista com todos os valores das expressões.
        Parâmetro: lista ---- é uma lista com as expressões a serem calculadas. Separa-se cada expressão da outra (quando há uma comparação entre elas)
                              por meio de um 'x', que também indica o momento em que uma expressão acaba.
    '''
    valor = int(lista[0])
    valores_expressoes = []
    for i in range(len(lista)):
        if lista[i] == '+':
            valor += int(lista[i + 1])
        if lista[i] == '-': 
            valor -= int(lista[i + 1])
        if lista[i] == 'x':
            valores_expressoes.append(int(valor))
            valor = int(lista[i + 1])
    valores_expressoes.append(valor)
    return valores_expressoes


def avaliar_comparacao(lista_valores, lista_operadores):
    '''A partir de uma lista com os valores a serem comparados e os operadores da operação, monta uma lista que contém ambos intercalados e - troca
    'AND' e 'OR' por um 'x', para indicar uma separação, visto que o valor da expressão com 'AND' e 'OR' é analisado em outra função
        Parâmetros: lista_valores ---- lista que contém todos os valores a serem comparados
                    lista_operadores ---- lista que contém todos os operadores a serem usados
    '''    
    lista_valor_operador = []
    lista_true_false = []
    for i in range(len(lista_valores)):
        lista_valor_operador.append(lista_valores[i])
        lista_valor_operador.append(lista_operadores[i])
    for i in range(len(lista_valor_operador)):
        if lista_valor_operador[i] in ['AND', 'OR']:
            lista_valor_operador[i] = 'x'
    valor = True
    for i in range(len(lista_valor_operador)):
        if lista_valor_operador[i] == '<':
            valor = valor and lista_valor_operador[i - 1] < lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == '<=':
            valor = valor and lista_valor_operador[i - 1] <= lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == '>':
            valor = valor and lista_valor_operador[i - 1] > lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == '>=':
            valor = valor and lista_valor_operador[i - 1] >= lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == '==':
            valor = valor and lista_valor_operador[i - 1] == lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == '!=':
            valor = valor and lista_valor_operador[i - 1] != lista_valor_operador [i + 1]
        elif lista_valor_operador[i] == 'x':
            lista_true_false.append(valor)
            valor = True
    return lista_true_false


def avaliar_and_or(lista_true_false, ands_or):
    '''Função que recebe uma lista com os valores lógicos True e False e uma lista com os operadores 'AND' ou 'OR', interala-os em uma lisa e faz
    a comparação entre eles retornando o valor lógico da expressão como um todo
        Parâmetros: lista_true_false ---- é a lista que contém os valores lógicos que sofrerão com operações
                    ands_or ---- é a lista que contém os operadores 'AND' ou 'OR' a serem aplicados para obter o resultado final
    '''    
    lista_comparacao_final = []
    for i in range(len(lista_true_false)):
        lista_comparacao_final.append(lista_true_false[i])
        try: 
            lista_comparacao_final.append(ands_or[i])
        except:
            continue
    valor = lista_comparacao_final[0]
    for i in range(len(lista_comparacao_final)):
        if lista_comparacao_final[i] == 'AND':
            valor = valor and (lista_comparacao_final[i + 1])
        elif lista_comparacao_final[i] == 'OR':
            valor = valor or (lista_comparacao_final[i + 1])
    return valor

def separa_expressoes(linha):
    '''Função que, dada uma string, faz uma lista com os caracteres/palavras dela separados por espaço. Percorre a lista e troca todos os seus 
    operadores (menos o de subtração e adição) por 'x', para retornar uma lista que contenha as expressões a serem calculadas separadamente por meio 
    do 'x'
        Parâmetros: linha ---- string a ter suas expressões separadas
    '''
    palavras = linha.split(' ')
    for i in range(len(palavras)):
        if (palavras[i])[0].isalpha() and not palavras[i] in ['AND', 'OR']:
            palavras[i] = int((variaveis[(palavras[i])]))
    l = palavras
    for i in range(len(palavras)):
        if palavras[i] in ['>', '>=', '<', '<=', '==', '!=', 'AND', 'OR']:
            l[i] = 'x'
    return l

def lista_de_operadores(linha):
    '''Função que, dada uma string, faz uma lista com os caracteres/palavras dela separados por espaço. Percorre a lista e extrai todos os seus
    operadores de comparação, para retornar uma lista que contenha tais operadores e um 'x' no final (questões de adequamento de índices para a utilização em outras funções)
        Parâmetros: linha ---- string a ter seus operadores de comparação extraidos
    '''
    lista_caracteres = linha.split(' ')
    lista_operadores = []
    for i in range(len(lista_caracteres)):
        if lista_caracteres[i] in ['>', '>=', '<', '<=', '==', '!=', 'AND', 'OR']:
            lista_operadores.append(lista_caracteres[i])
    lista_operadores.append('x')
    return lista_operadores

def lista_and_or(linha):
    '''Função que, dada uma string, chama a função lista_de_operadores para tal string e extrai os operadores 'AND' e 'OR' da lista retornada pela função
    anteriormente chamada, retorna uma lista com tais operadores 
        Parâmetros: linha ---- string a ter seus operadores 'AND' e 'OR' extraidos
    '''
    ands_or = []
    for i in lista_de_operadores(linha):
        if i in ['AND', 'OR']:
            ands_or.append(i)
    return ands_or

def avaliacao_completa(linha):
    '''Avalia expressões complexas, que tenham comparações e não apenas algebra. Retorna o valor obtido.
        Parâmetros: linha ---- string a ser avaliada
    '''
    return avaliar_and_or(avaliar_comparacao(avaliar_algebra(separa_expressoes(linha)), lista_de_operadores(linha)), lista_and_or(linha))

def avaliacao_algebrica(linha):
    '''Avalia expressões simples que contenam apenas operações algébricas. Retorna o valor obtido.
        Parâmetros: linha ---- string a ser avaliada
    '''
    return avaliar_algebra(separa_expressoes(linha))

variaveis = {} #DIcionário para armazenar as variáveis que serão - eventualmente - definidas
def tipos_entrada(linha):
    '''Função que analisa o tipo de entrada recebida (com ou sem atribuição, com ou sem comparação, com ou sem variáveis indefinidas, com ou sem nomes
    incorretos para variáveis) e faz a análise da entrada recebida dependendo do seu tipo, podendo imprimir erros sem fazer a análise caso algo da entrada
    esteja incorreto. Para essa análise, primeiro transforma a string em uma lista de palavras/caracteres separando-a por espaço
        Parâmetros: linha ---- string a ser avaliada
    '''
    palavras = linha.split(' ')
    variavel_ja_definida = True
    if len(palavras) > 1 and palavras[1] == '=': #Entrada com atribuição
        tem_comparacao = False
        for i in palavras:
            if i in ['>', '>=', '<', '<=', '==', '!=', 'AND', 'OR']:
                tem_comparacao = True
                break
        variavel_valida = True
        if not palavras[0].isalnum():
            variavel_valida = False
        elif palavras[0][0].isnumeric():
            variavel_valida = False
        if variavel_valida == False:
            return(f'Erro de sintaxe: {palavras[0]} nao e um nome permitido para uma variavel.')
        for i in range(1, len(palavras)):
            try:
                if (palavras[i])[0].isalpha() and not palavras[i] in ['AND', 'OR']:
                    palavras[i] = int((variaveis[(palavras[i])]))
            except:
                variavel_ja_definida = False
                return(f'Erro de referencia: a variavel {palavras[i]} nao foi definida.')
        else:
            if tem_comparacao == True:
                variaveis[palavras[0]] = avaliacao_completa(linha[len(palavras[0]) + 3:])
            else:
                variaveis[palavras[0]] = avaliacao_algebrica(linha[len(palavras[0]) + 3:])[0]
    else: #Entrada sem atribuição
        tem_comparacao = False
        for i in range(len(palavras)):
            try:
                if (palavras[i])[0].isalpha() and not palavras[i] in ['AND', 'OR']:
                    palavras[i] = int((variaveis[(palavras[i])]))
            except:
                variavel_ja_definida = False
                return(f'Erro de referencia: a variavel {palavras[i]} nao foi definida.')
        if variavel_ja_definida == True:
            for i in palavras:
                if i in ['>', '>=', '<', '<=', '==', '!=', 'AND', 'OR']:
                    tem_comparacao = True
                    break
            if tem_comparacao == True:
                return avaliacao_completa(linha)
            else:
                return avaliacao_algebrica(linha)[0]

def main():
    '''Função principal que unifica todas as outras, recebendo os inputs e trabalhando para imprimir seus retornos corretamente,até 
    que seja obtido um EOFError e encerrando o processo em tal momento e imprimindo uma mensagem final
        Parâmetros: sem parâmetros
    '''
    while True:
        try:
            linha = input()
            x = tipos_entrada(linha)
            if x == True:
                print(1)
            elif x == False:
                print(0)
            elif x != None:
                print(x)
        except EOFError:
            print('Encerrando... Bye-bye.')
            break

main()