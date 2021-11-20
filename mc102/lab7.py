def codificacao_hexadecimal(string, enxerto):
  ''' 
  Codifica a string de entrada da maneira desejada para os casos de linha ímpar,
  ou seja, quando usa-se o sistema hexadecimal \n
  Parâmetros:
            string = entrada a ser codificada \n
            enxerto = número que indica o enxerto usado na conversão
  '''
  lista_ascii = []
  for i in string:
    x = hex(ord(i))[2:]
    lista_ascii.append(str(x).zfill(enxerto))
  string_convertida = ''
  for i in lista_ascii:
    string_convertida += i.upper()
  return string_convertida


def codificacao_octal(string, enxerto):
  ''' 
  Codifica a string de entrada da maneira desejada para os casos de linha par,
  ou seja, quando usa-se o sistema octal. \n
  Parâmetros:
            string = entrada a ser codificada \n
            enxerto = número que indica o enxerto usado na conversão
  '''
  lista_octal = []
  string_invertida = string[::-1]
  for i in string_invertida:
    x = oct(ord(i))[2:]
    lista_octal.append(str(x).zfill(enxerto))
  string_convertida = ''
  for i in lista_octal:
    string_convertida += i
  return string_convertida



def decodifica(string, enxerto, base):
    '''
    Decodifica um número usando as regras de codificação já usadas nas funções de decodificação \n
    Parâmetros:
            string = entrada a ser decodificada \n
            enxerto = número que indica o enxerto a ser usado na decodificação \n
            base = número que indica em qual base foi codificada a string a ser decodificada             
    '''
    lista_caracteres = []
    for i in range(0, len(string), enxerto):
        lista_caracteres.append(string[i:i+enxerto])
    if base == 8:
        lista_caracteres.reverse()
    string_decodificada = ''
    for i in lista_caracteres:
        x = int(i, base)
        string_decodificada += chr(x)
    return string_decodificada

#Pegando o primeiro input, que possui o modo, o enxerto e número de linhas e colocando tais informações em variáveis separadas
modo_enxerto_linhas = input() 
modo = modo_enxerto_linhas.split(' ')[0]
enxerto = modo_enxerto_linhas.split(' ')[1]
linhas = modo_enxerto_linhas.split(' ')[2]

#Criando uma lista que armazena os inputs de cada linha com as informações a serem codificadas ou decodificadas
lista_inputs = []
i = 1
while i <= int(linhas):
    x = input()
    lista_inputs.append(x) 
    i += 1

#Aplicando as codificações/decodificações (dependendo do modo escolhido no primeiro input) das funções 
#já definidas (dependendo da posição da linha (se é par ou ímpar)), armazenando as saídas em listas e imprimindo-os

if modo == '1':
    lista_saidas = []
    for i in range(len(lista_inputs)):
        if i % 2 != 0:
            x = codificacao_octal(lista_inputs[i], int(enxerto))
            lista_saidas.append(x)
        else:
            x = codificacao_hexadecimal(lista_inputs[i], int(enxerto))
            lista_saidas.append(x)
    for i in lista_saidas:
        print(i)

if modo == '2':
    lista_saidas = []
    for i in range(len(lista_inputs)):
        if i % 2 != 0:
            x = decodifica(lista_inputs[i], int(enxerto), 8)
            lista_saidas.append(x)
        else:
            x = decodifica(lista_inputs[i], int(enxerto), 16)
            lista_saidas.append(x)
    for i in lista_saidas:
        print(i)
