dia_semana_e_numero = input() #Pega o dia da semana e o número separados por um espaço
lista_dia_semana_e_numero = dia_semana_e_numero.split(" ") #Cria uma lista de dois elementos, sendo o primeiro o dia da semana e o
                                                           #segundo o número de dados que será colocado
dia_semana = lista_dia_semana_e_numero[0] #String com o dia da semana
numero = int(lista_dia_semana_e_numero[1]) #Inteiro do número de dados

def pegar_enderecos(numero):
    ''' A função usa o número de dados obtido anteriormente e pega a quantidade de endereços correspondente a tal número,
    retornando uma lista com todos esses endereços.
    '''
    lista_enderecos = []
    for i in range(numero):
        endereco = input()
        lista_enderecos.append(endereco)
    return lista_enderecos

lista_enderecos = pegar_enderecos(numero) #Criando lista de endereços como uma variável global

def numero_letras_maiusculas(i):
    ''' A função pega uma string qualquer e computa o número de letras maiúsculas dela, retornando esse mesmo valor. 
    '''
    lista = list(i)
    n = 0
    for k in lista:
        if k.isalpha() and k.isupper():
            n += 1
    return n

def numero_letras_minusculas(i):
    ''' A função pega uma string qualquer e computa o número de letras minúsculas dela, retornando esse mesmo valor.
    '''
    lista = list(i)
    n = 0
    for k in lista:
        if k.isalpha() and k.islower():
            n += 1
    return n

def numero_letras_geral(i):
    ''' A função pega uma string qualquer e computa o número de letras dela, retornando esse mesmo valor. 
    '''
    lista = list(i)
    n = 0
    for k in lista:
        if k.isalpha():
            n += 1
    return n

def numero_palavras(i):
    ''' A função pega uma string qualquer e computa o número de palavras dela, retornando esse mesmo valor.
    '''
    lista_palavras = i.split(" ")
    n = len(lista_palavras)
    return n

def soma_ascii(i):
    ''' A função pega uma string qualquer e computa a soma dos valores ascii de todos os seus caracteres, inclusive dos espaços.
    Retorna o valor de tal soma.
    '''
    soma = 0
    lista = list(i)
    for k in lista:
        soma += ord(k)
    return soma

def imprimindo_dados():
    ''' A função, sem nenhum parâmetro, imprime diferentes saídas para o programa de acordo com o dia da semana correspondente.
    '''
    if dia_semana == "Segunda":
        l = sorted(lista_enderecos, key=numero_letras_minusculas)
        for i in l:
            print(i)
    elif dia_semana == "Terca":
        l = sorted(lista_enderecos, key=numero_letras_maiusculas, reverse=True)
        for i in l:
            print(i)
    elif dia_semana == "Quarta":
        l = sorted(lista_enderecos, key=numero_letras_geral)
        for i in l:
            print(i)
    elif dia_semana == "Quinta":
        l = sorted(lista_enderecos, key=numero_palavras)
        for i in l:
            print(i)
    elif dia_semana == "Sexta":
        l = sorted(lista_enderecos, key=soma_ascii, reverse=True)
        for i in l:
            print(i)
    
imprimindo_dados() #Chamando a função para imprimir todos os dados necessários