#Faça uma função que inverte um dicionário mesmo quando várias chaves tem o mesmo valor associdado.
#Dica: use um conjunto para representar as várias chaves

def inverte(dicionario):
    novo_dicionario = {}
    for chave, valor in dicionario.items():
        if valor not in novo_dicionario.keys():
            novo_dicionario[valor] = set([chave])
        else:
            novo_dicionario[valor].add(chave)
    return novo_dicionario

dicionario = {1: 'ana', 2: 'beto', 3: 'ana'}

print(inverte(dicionario))