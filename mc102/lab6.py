class Medalutador:
    def __init__(self, ID, medapecas, habilidade, recuperacao_habilidade):
        ''' Inicialização de um objeto da classe
        Parâmetros:
            ID === id do medalutador
            medapecas === medapecas do medalutador
            habilidade === habilidade do medalutador
            recuperacao_habilidade === recuperacao de habilidade do medalutador
        '''
        self.ID = ID
        self.medapecas = medapecas
        self.habilidade = habilidade
        self.medabot = Medabot(self.medapecas)
        self.recuperacao_habilidade = recuperacao_habilidade
        self.habilidade_inicial = habilidade

    def obter_ID(self):
        ''' Método que retorna o ID do medalutador analisado.
        Parâmetros: 
            self === medalutador analisado
        '''
        return self.ID

    def obter_recuperacao(self):
        ''' Método que retorna a recuperação do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return self.recuperacao_habilidade

    def obter_habilidade(self):
        ''' Método que retorna a habilidade do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return self.habilidade

    def obter_habilidade_inicial(self):
        ''' Método que retorna a habilidade inicial do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return self.habilidade_inicial

    def melhor_peca_para_pegar(self, medalutador_adversario):
        ''' Método que analisa todas as medapecas disponíveis e determina quais são as melhores de cada tipo para
        o medalutador vencedor da batalha tomar do medalutador perdedor, fazendo a transferência de peças
        Parâmetros:
            self === medalutador vencedor da batalha
            medalutador_adversario === medalutador perdedor
        '''
        diferenca_torso = - (self.obter_pts_torso() - medalutador_adversario.obter_pts_torso())
        diferenca_braco_e = - (self.obter_pts_braco_e() - medalutador_adversario.obter_pts_braco_e())
        diferenca_braco_d = - (self.obter_pts_braco_d() - medalutador_adversario.obter_pts_braco_d())
        diferenca_pernas = - (self.obter_pts_pernas() - medalutador_adversario.obter_pts_pernas())
        maior_valor = max(diferenca_torso, diferenca_braco_e, diferenca_braco_d, diferenca_pernas)

        if maior_valor == diferenca_torso:
            pts_torso = medalutador_adversario.obter_pts_torso()
            (self.medapecas).append('T ' + str(pts_torso))
            (medalutador_adversario.medapecas).remove('T ' + str(pts_torso))
        elif maior_valor == diferenca_braco_e:
            pts_braco_e = medalutador_adversario.obter_pts_braco_e()
            (self.medapecas).append('E ' + str(pts_braco_e))
            (medalutador_adversario.medapecas).remove('E ' + str(pts_braco_e))
        elif maior_valor == diferenca_braco_d:
            pts_braco_d = medalutador_adversario.obter_pts_braco_d()
            (self.medapecas).append('D ' + str(pts_braco_d))
            (medalutador_adversario.medapecas).remove('D ' + str(pts_braco_d))
            
        elif maior_valor == diferenca_pernas:
            pts_pernas = medalutador_adversario.obter_pts_pernas()
            (self.medapecas).append('P ' + str(pts_pernas))
            (medalutador_adversario.medapecas).remove('P ' + str(pts_pernas))
    
    def obter_pts_torso(self):
        ''' Método que retorna os pontos de torso do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[0].split(' ')[1])

    def obter_pts_pernas(self):
        ''' Método que retorna os pontos das pernas do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[1].split(' ')[1])
    
    def obter_pts_braco_d(self):
        ''' Método que retorna os pontos do braço direito do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[2].split(' ')[1])
    
    def obter_pts_braco_e(self):
        ''' Método que retorna os pontos do braço esquerdo do medalutador analisado.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[3].split(' ')[1])

    def obter_bonus_atk(self):
        ''' Método que retorna os pontos do bonus de ataque do medalutador analisado devido à medalha.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[4].split(' ')[0])
        
    def obter_bonus_def(self):
        ''' Método que retorna os pontos do bonus de defesa do medalutador analisado devido à medalha.
        Parâmetros:
            self === medalutador analisado
        '''
        return int((self.medabot).pega_melhor_peca()[4].split(' ')[1])

    def obter_ataque(self):
        ''' Método que retorna o ataque total do medabot, que é o mesmo ataque do medalutador.
        Parâmetros:
            self === medalutador que desejamos obter o ataque
        '''
        melhores_pecas = (self.medabot).pega_melhor_peca()
        braco_d = int(melhores_pecas[2].split(' ')[1])
        braco_e = int(melhores_pecas[3].split(' ')[1])
        atk_medalha = int(melhores_pecas[4].split(' ')[0])
        return braco_d + braco_e + atk_medalha
        
    def obter_defesa(self):
        ''' Método que retorna o defesa total do medabot, que é a mesma defesa do medalutador.
        Parâmetros:
            self === medalutador que desejamos obter o defesa
        '''
        melhores_pecas = (self.medabot).pega_melhor_peca()
        torso = int(melhores_pecas[0].split(' ')[1])
        perna = int(melhores_pecas[1].split(' ')[1])
        def_medalha = int(melhores_pecas[4].split(' ')[1])
        return torso + perna + def_medalha


    def atualiza_habilidade(self, perdedor):
        ''' Método que atualiza a habilidade dos medalutadores após uma batalha.
        Parâmetros:
            self === medalutador vencedor
            perdedor === medalutador perdedor
        '''
        if self.habilidade - perdedor.habilidade > 0:
            self.habilidade = min(self.obter_habilidade() - perdedor.habilidade + self.obter_recuperacao(), self.obter_habilidade_inicial())
        else:
            self.habilidade = min(self.obter_habilidade_inicial(), self.obter_recuperacao())
        perdedor.habilidade = min(perdedor.obter_habilidade() // 2 + perdedor.obter_recuperacao(), perdedor.obter_habilidade_inicial())
    
    def atualiza_medabot(self):
        ''' Método que atualiza o medabot associado ao medalutador.
        Parâmetros:
            self === medalutador ao qual o medabot está associado
        '''
        self.medabot = Medabot(self.medapecas)

    def __repr__(self):
        return str(self.ID)


class Medabot:
    def __init__(self, medapecas):
        ''' Inicialização de um objeto da classe.
        Parâmetros:
            medapecas === medapecas do medalutador ao qual o medabot esta associado
        '''
        self.medapecas = medapecas


    def separa_pecas(self):
        ''' Método que separa as medapeças disponiveis em categorias correspondentes aos seus tipos
        Parâmetros:
            self === medabot que tem acesso às medapecas disponíveis
        '''
        torsos = []
        pernas = []
        bracos_direitos = []
        bracos_esquerdos = []
        medalha = []
        for medapeca in self.medapecas:
            if medapeca.split(' ')[0] == 'P':
                pernas.append(medapeca)
            elif medapeca.split(' ')[0] == 'E':
                bracos_esquerdos.append(medapeca)
            elif medapeca.split(' ')[0] == 'D':
                bracos_direitos.append(medapeca)
            elif medapeca.split(' ')[0] == 'T':
                torsos.append(medapeca)
            else:
                medalha.append(medapeca)
        return torsos, pernas, bracos_direitos, bracos_esquerdos, medalha
    

    def pega_melhor_peca(self):
        ''' Método que analisa todas as medapecas disponíveis e determina quais são as melhores de cada tipo para
        montar o medabot que irá para a batalha
        Parâmetros:
            self === medabot analisado
        '''
        pecas = self.separa_pecas()
        torsos = [x.split(' ')[1] for x in pecas[0]]
        melhor_torso = 'T ' + str(max(torsos))
        pernas = [x.split(' ')[1] for x in pecas[1]]
        melhor_perna = 'P ' + str(max(pernas))
        bracos_direitos = [x.split(' ')[1] for x in pecas[2]]
        melhor_braco_direito = 'D ' + str(max(bracos_direitos))
        bracos_esquerdos = [x.split(' ')[1] for x in pecas[3]]
        melhor_braco_esquerdo = 'E ' + str(max(bracos_esquerdos))
        medalha = pecas[4][0]

        return melhor_torso, melhor_perna, melhor_braco_direito, melhor_braco_esquerdo, medalha


def batalhar(i, j):
    ''' Função que faz as batalhas entre dois medalutadores, retornando seu vencedor e atualizando as habilidades
    e medapecas de cada um dos medalutadores
    Parâmetros:
        i === medalutador qualquer 
        j === medalutador adversario à i
    '''
    i.atualiza_medabot()
    j.atualiza_medabot()
    habilidade_i, habilidade_j = i.obter_habilidade(), j.obter_habilidade()
    ataque_i, ataque_j = i.obter_ataque(), j.obter_ataque()
    defesa_i, defesa_j = i.obter_defesa(), j.obter_defesa()
    id_i, id_j = i.obter_ID(), j.obter_ID()

    if (ataque_i > defesa_j or ataque_j > defesa_i) and ataque_i - defesa_j != ataque_j - defesa_i:
        if ataque_i - defesa_j > ataque_j - defesa_i:
            vencedor, perdedor = i, j
        else:
            vencedor, perdedor = j, i
    elif habilidade_i != habilidade_j:
        if habilidade_i > habilidade_j:
            vencedor, perdedor = i, j
        else:
            vencedor, perdedor = j, i
    else:
        if id_i < id_j:
            vencedor, perdedor = i, j
        else:
            vencedor, perdedor = j, i
    vencedor.atualiza_habilidade(perdedor)
    vencedor.melhor_peca_para_pegar(perdedor)

    return vencedor

def imprimir_resultado_da_batalha(k):
    ''' Função que imprime o resultado da batalha a partir de seus vencedor.
    Parâmetro:
        k === medalutador vencedor da batalha
    '''
    tipo_medapeca = (k.medapecas[len(k.medapecas) - 1]).split(' ')[0]
    pts_medapeca = (k.medapecas[len(k.medapecas) - 1]).split(' ')[1]
    print(f'Medalutador {k} venceu e recebeu a {tipo_medapeca}{pts_medapeca}\n')


def imprimir_ficha_tecnica(i, j):
    ''' Função que imprime a ficha técnica de dois medalutadores adversários i e j.
    Parâmetros:
        i === medalutador i qualquer
        j === medalutador j adversário de i
    '''
    for k in [i, j]:
        print(f'\tA{k.obter_ID()} = E{k.obter_pts_braco_e()} + D{k.obter_pts_braco_d()} + {k.obter_bonus_atk()} = {k.obter_ataque()}')
        print(f'\tD{k.obter_ID()} = T{k.obter_pts_torso()} + P{k.obter_pts_pernas()} + {k.obter_bonus_def()} = {k.obter_defesa()}')
        print(f'\tH{k.obter_ID()} = {k.obter_habilidade()}')

def simular_torneios_de_cyberlutas(lista_de_medalutadores):
    ''' Função que simula o torneio de cyberlutas como um todo.
    Parâmetro:
        lista_de_medalutadores === lista com todos os objetos da classe Medalutador que irão participar do torneio.
    '''
    lista_torneio_principal = []
    lista_de_repescagem     = []
    for medalutador in lista_de_medalutadores:
        lista_torneio_principal.append(medalutador)
    while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
        lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
        lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
    i = lista_torneio_principal.pop(0)
    j = lista_de_repescagem.pop(0)
    print('Cyberluta Final')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    print(f'Campeao: medalutador {k}')
  
def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
    ''' Função que aplica uma rodade de batalhas do torneio.
    Parâmetros:
        lista_de_medalutadores === lista com todos os objetos da classe Medalutador que ainda permanecem no torneio.
        lista_de_repescagem === lista com todos os objetos da classe Medalutador que estão na parte de repescagem do torneio.
    '''
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores
    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0) 
        j = lista_de_medalutadores.pop(0)
        if i.obter_ID() > j.obter_ID():
            i, j = j, i
        if lista_de_repescagem != None:
            print('Cyberluta do Torneio Principal')
        else:
            print('Cyberluta da Repescagem')
        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)
        k = batalhar(i, j)
        imprimir_resultado_da_batalha(k)
        if lista_de_repescagem != None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)
        lista_de_vencedores.append(k)
    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores

def main():
    ''' Função principal do programa que organiza as entradas e chama as outras funções necessárias para o funcionamento deste.
    Parâmetros:
        sem parâmetros
    '''
    lista_de_medalutadores = []
    numero_de_medalutadores = int(input())
    for i in range(numero_de_medalutadores):
        h_r_nmedapecas = input()
        habilidade = int(h_r_nmedapecas.split(' ')[0])
        recuperacao = int(h_r_nmedapecas.split(' ')[1])
        numero_medapecas = int(h_r_nmedapecas.split(' ')[2])
        medapecas = []
        for j in range(numero_medapecas + 1):
            medapecas.append(input())
        lista_de_medalutadores.append(Medalutador(i + 1, medapecas, habilidade, recuperacao))

    simular_torneios_de_cyberlutas(lista_de_medalutadores)
main()
