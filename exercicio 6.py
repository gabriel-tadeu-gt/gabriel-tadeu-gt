#Faça uma função que, dada uma lista, devolve uma lista sem elementos repetidos.
#Dica: use conjuntos

lista = [1, 1, 2, 3, 3, 2, 'a', 'a', 'b']

def sem_repeticao(l):
    return list(set(l))

print(sem_repeticao(lista))

#sem conjuntos (mantém a ordem)
#def sem_repeticao(l):
#    nova_lista = []
#    for i in l:
#        if i not in nova_lista:
#            nova_lista.append(i)
#    return nova_lista