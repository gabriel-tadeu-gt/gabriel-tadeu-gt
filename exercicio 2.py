#Faça uma função que, dados conjuntos s1 e s2 devolve um novo conjunto representando a interseção de s1 e s2

s1 = {1, 2, 3, 12, 5, 6}
s2 = {5, 1, 3, 10, 11, 12}

def intersecao(s1, s2):
    conjunto_intersecao = set()
    for i in s1:
        if i in s2:
            conjunto_intersecao.add(i)
    return conjunto_intersecao

print(intersecao(s1, s2))
