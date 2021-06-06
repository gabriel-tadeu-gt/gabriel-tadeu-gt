#Faça uma função que, dados conjuntos s1 e s2 devolve se um dos conjuntos é subconjunto do outro

def subconjunto(s1, s2):
    s1subconjunto = True
    s2subconjunto = True
    for i in s2:
        if not i in s1:
            s2subconjunto = False
            break
    for i in s1:
        if not i in s2:
            s1subconjunto = False
            break
    return s1subconjunto, s2subconjunto


s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 5, 6, 5, 6, 3, 10, 11, 12}

print(subconjunto(s1, s2))