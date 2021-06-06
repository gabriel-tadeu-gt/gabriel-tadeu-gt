#Faça uma função que, dados conjuntos s1 e s2 devolve um novo conjunto representando a subtração de s1 e s2

def subtracao(s1, s2):
    conjunto_subtracao = set()
    for i in s1:
        if not i in s2:
            conjunto_subtracao.add(i)
    return conjunto_subtracao

s1 = {1, 2, 3, 12, 5, 6}
s2 = {5, 6, 3, 10, 11, 12}

print(subtracao(s1, s2))