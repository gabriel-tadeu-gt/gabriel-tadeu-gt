#A ideia é criar uma lista de dicionários com as características de cada suspeito organizadas nesses dicionários

def verifica_tipo_linha(linha):
    ''' Função que vê qual é o tipo de linha que foi digitada como entrada. Retorna o tipo do input 
    usado como parâmetro no contexto do lab
        Parâmetro: linha ---- string que será verficada
    '''
    tipo_linha = ''
    if linha == '-':
        #novo dicionário de um suspeito
        tipo_linha = 'separador_novo_supeito'
    elif linha == '--':
        #dicionário com características gerais a serem procuradas
        tipo_linha = 'separador_suspeitos_evidencias'
    elif linha == '---':
        #fim da entrada
        tipo_linha = 'fim_dossie'
    else:
        #entrada normal 
        tipo_linha = 'nova_caracteristica'
    return tipo_linha

def pede_nova_linha():
    ''' Função responsável por pedir novas características e evidências por meio de mais inputs
        Sem parâmetros, retorna uma lista com uma ficha de cada suspeito e uma ficha de evidências na
        forma de dicionários
    '''
    lista_das_fichas = []
    lista_de_suspeitos_evidencias = []
    ficha_novo_suspeito = {}
    ficha_evidencias = {}
    eh_evidencia = False 
    while True:
        linha = input()
        linha_sem_espaços_fim_inicio = linha.strip()
        tipo_linha = verifica_tipo_linha(linha_sem_espaços_fim_inicio)
        
        if tipo_linha == 'separador_suspeitos_evidencias':
            eh_evidencia = True

        if eh_evidencia == False:
            if tipo_linha == 'nova_caracteristica':
                tipo_caracteristica = linha_sem_espaços_fim_inicio.split(':')
                tipo = tipo_caracteristica[0].strip()
                caracteristica = tipo_caracteristica[1].strip()
                ficha_novo_suspeito[tipo] = caracteristica
            
            elif tipo_linha == 'separador_novo_supeito':
                lista_das_fichas.append(ficha_novo_suspeito)
                ficha_novo_suspeito = {}
        
        if eh_evidencia == True and tipo_linha == 'nova_caracteristica':
            tipo_caracteristica = linha_sem_espaços_fim_inicio.split(':')
            tipo = tipo_caracteristica[0].strip()
            caracteristica = tipo_caracteristica[1].strip()
            ficha_evidencias[tipo] = caracteristica

        if tipo_linha == 'fim_dossie':
            lista_das_fichas.append(ficha_novo_suspeito)
            break

    lista_de_suspeitos_evidencias.append(lista_das_fichas)
    lista_de_suspeitos_evidencias.append(ficha_evidencias)
    return lista_de_suspeitos_evidencias


def compara_suspeitos_com_evidencias():
    ''' Função que compara as fichas dos suspeitos com as fichas das evidências de acordo com as especificações
    dadas para veriicar quais suspeitos devem ser retornados após a filtragem das características
        Sem parâmetros, retorna a lista com os suspeitos a serem impressos no final do programa
    '''
    lista_de_suspeitos_evidencias = pede_nova_linha()
    fichas_suspeitos = lista_de_suspeitos_evidencias[0]
    ficha_evidencias = lista_de_suspeitos_evidencias[1]
    caracteristicas_necessarias = set(list(ficha_evidencias.keys()))
    lista_criminosos = []

    for suspeito in fichas_suspeitos:
        caracteristicas_suspeito = set(list(suspeito.keys()))
        if caracteristicas_necessarias.issubset(caracteristicas_suspeito):
            for caracteristica in caracteristicas_necessarias:
                eh_suspeito_valido = True
                if suspeito[caracteristica] != ficha_evidencias[caracteristica]:
                    eh_suspeito_valido = False
                    break
            if eh_suspeito_valido:
                lista_criminosos.append(suspeito['Nome'])


    return lista_criminosos


#Chamada da função de comparação dos suspeitos com as evidências e impressão das saídas adeqadas com
#a quantidade de suspeitos encontrada
lista_criminosos = compara_suspeitos_com_evidencias()

if len(lista_criminosos) == 0:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')

elif len(lista_criminosos) == 1:
    print('Suspeito(a):')
    print(lista_criminosos[0])

else:
    print('Suspeitos(as):')
    lista_criminosos_ordenada = sorted(lista_criminosos)
    for i in lista_criminosos_ordenada:
        print(i)
