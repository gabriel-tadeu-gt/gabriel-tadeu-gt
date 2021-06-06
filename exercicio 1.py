#Faça uma função que, dados conjuntos s1 e s2 devolve um novo conjunto representando a união de s1 e s2

s1 = {1, 2, 3, 4, 5, 6}
s2 = {7, 8, 9, 10, 11, 12}

def uniao(s1, s2):
    conjunto_uniao = set()
    for i in s1:
        conjunto_uniao.add(i)
    for i in s2:
        conjunto_uniao.add(i)
    return conjunto_uniao

print(uniao(s1, s2))
