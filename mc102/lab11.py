
def calcula_distancia(coordenada_y, ponto_qualquer):
    x_ponto, y_ponto = ponto_qualquer[0], ponto_qualquer[1]
    return ((x_ponto) ** 2 + (y_ponto - coordenada_y) ** 2) ** 0.5


def esconderijo_mais_distante_em_relacao_ao_ponto(coordenada_y, lista_esconderijos):
    esconderijo_mais_distante = lista_esconderijos[0]
    distancia_esconderijo_mais_distante = calcula_distancia(coordenada_y, esconderijo_mais_distante)
    for esconderijo in range(1, len(lista_esconderijos)):
        distancia = calcula_distancia(coordenada_y, lista_esconderijos[esconderijo])
        if distancia > distancia_esconderijo_mais_distante:
            esconderijo_mais_distante = lista_esconderijos[esconderijo]
            distancia_esconderijo_mais_distante = distancia
    return coordenada_y, esconderijo_mais_distante, distancia_esconderijo_mais_distante


def busca_binaria_intervalos(coordenada_y, lista_esconderijos):
    primeiro = 0
    ultimo = coordenada_y - 1
    while primeiro < ultimo:
        meio = (primeiro + ultimo) // 2
        m = esconderijo_mais_distante_em_relacao_ao_ponto(meio, lista_esconderijos)
        p = esconderijo_mais_distante_em_relacao_ao_ponto(primeiro, lista_esconderijos)
        u = esconderijo_mais_distante_em_relacao_ao_ponto(ultimo, lista_esconderijos)
        distancia_meio = float(m[2])
        distancia_primeiro = float(p[2])
        distancia_ultimo = float(u[2])
        m_1 = esconderijo_mais_distante_em_relacao_ao_ponto(meio + 1, lista_esconderijos)
        distancia_meio_mais_um = m_1[2]
        if distancia_meio < distancia_primeiro:
            if distancia_meio_mais_um > distancia_meio:
                ultimo = meio
            else:
                primeiro = meio + 1 #ou ultimo = meio - 1
        elif distancia_meio > distancia_primeiro:
            ultimo = meio
        else:
            if distancia_primeiro < distancia_ultimo:
                return primeiro
            elif distancia_ultimo < distancia_primeiro:
                return ultimo
    if distancia_primeiro < distancia_ultimo:
        return primeiro
    else:
        return ultimo

def olha_acima_abaixo(m, lista_esconderijos):
    x0 = esconderijo_mais_distante_em_relacao_ao_ponto(m - 1, lista_esconderijos)
    x1 = esconderijo_mais_distante_em_relacao_ao_ponto(m, lista_esconderijos)
    x2 = esconderijo_mais_distante_em_relacao_ao_ponto(m + 1, lista_esconderijos)
    d0 = x0[1]
    d1 = x1[1]
    d2 = x2[1]
    minimo = min([d0, d1, d2])
    if d0 == minimo:
        return m - 1
    elif d1 == minimo:
        return m
    elif d2 == minimo:
        return m + 1

def pega_inputs_trabalha():
    lista_respostas = []
    while True:
        x = input()
        if x != '0 0':
            lx = x.split(' ')
            coordenada_muralha = int(lx[1])
            numero_esconderijos = int(lx[0])
            lista_esconderijos = []
            for i in range(numero_esconderijos):
                l = []
                linha = input()
                l.append(int(linha.split(' ')[0]))
                l.append(int(linha.split(' ')[1]))
                t = tuple(l)
                lista_esconderijos.append(t)
            lista_respostas.append(busca_binaria_intervalos(coordenada_muralha, lista_esconderijos))
        else:
            return lista_respostas

l = pega_inputs_trabalha()
for i in l:
    print(i)


