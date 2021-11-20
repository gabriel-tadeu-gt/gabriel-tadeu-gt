def testa_tentativa(tentativa, senha_mestre):
    ''' Função que testa se a tentativa é igual à senha mestre fornecida.
    Parâmetros:
        tentativa === inteiro que corresponde à tentativa do usuário
        senha_mestre === inteiro que corresponde à senha mestre
    '''
    acertou = False
    if tentativa == senha_mestre: #Caso o usuário acerte a senha, dá o aviso de senha reconhecida e para de pegar tentativas
        acertou = True
    return acertou

def verifica_quantidade_digitos(tentativa, senha_mestre):
    ''' Função que testa se a tentativa possui a mesma quantidade de dígitos da senha mestre fornecida.
    Parâmetros:
        tentativa === inteiro que corresponde à tentativa do usuário
        senha_mestre === inteiro que corresponde à senha mestre
    '''
    mesma_quantidade_digitos = False
    if len(str(senha_mestre)) == len(str(tentativa)):
        mesma_quantidade_digitos = True
    return mesma_quantidade_digitos

def verifica_semelhanca(tentativa, senha_mestre):
    ''' Função que verifica qual é a quantidade de caracteres iguais no mesmo lugar na tentativa e na senha mestre fornecida.
    Parâmetros:
        tentativa === inteiro que corresponde à tentativa do usuário
        senha_mestre === inteiro que corresponde à senha mestre
    '''
    semelhanca = 0
    lista_tentativa = list(str(tentativa))
    lista_senha_mestre = list(str(senha_mestre))
    for i in range(len(lista_tentativa)):
        if lista_tentativa[i] == lista_senha_mestre[i]:
            semelhanca += 1
    return semelhanca

def main():
    ''' Função principal do programa, responsável por receber as entradas, chamar as outras funções necessárias e
    imprimir as saídas da maneira pedida.
    Parâmetros:
        Sem parâmetros
    '''
    aux = (input()).split(' ')
    senha_mestre = int(aux[0])
    numero_tentativas = int(aux[1])
    for i in range(numero_tentativas):
        tentativa = int(input())
        tentativas_restantes = numero_tentativas - 1 - i
        if testa_tentativa(tentativa, senha_mestre):
            print('Senha reconhecida. Desativando defesas...')
            break
        else:
            print('Senha incorreta')
            if not verifica_quantidade_digitos(tentativa, senha_mestre):
                print('Semelhanca: Erro: quantidade de digitos incongruente')
            else:
                print(f'Semelhanca: {verifica_semelhanca(tentativa, senha_mestre)}')
            print(f'Tentativas restantes: {tentativas_restantes}')
            print('')
            if tentativas_restantes == 0:
                print('Tentativas esgotadas. Acionando defesas...')
main()
