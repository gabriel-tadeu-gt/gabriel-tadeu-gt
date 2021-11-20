#Obtendo o nome do canal e a quantidade de dados que serão fornecidos
canal = input() 
numero_dados = int(input())

soma2018 = 0
soma2019 = 0
soma2020 = 0

anotacoes_trienio = 0
anotacoes_2018 = 0
anotacoes_2019 = 0
anotacoes_2020 = 0

visualizacoes_trienio = 0

#Obtendo todos os numero_dados que serão fornecidos, dividindo as datas por anos, obtendo os totais de visualizações por cada um dos anos 2018, 2019 e 2020.
#Ao mesmo tempo, também se obterá o número de anotações em cada um dos 3 anos e total de anotações no triênio.
for i in range(numero_dados):
    data = input().split("-")
    numero_visualizacoes = int(input())
    if data[0] == "2018":
        soma2018 += numero_visualizacoes
        anotacoes_trienio += 1
        anotacoes_2018 += 1
        visualizacoes_trienio += numero_visualizacoes
    elif data[0] == "2019":
        soma2019 += numero_visualizacoes
        anotacoes_trienio += 1
        anotacoes_2019 += 1
        visualizacoes_trienio += numero_visualizacoes
    elif data[0] == "2020":
        soma2020 += numero_visualizacoes
        anotacoes_trienio += 1
        anotacoes_2020 += 1
        visualizacoes_trienio += numero_visualizacoes
    else:
        continue

total_trienio = soma2018 + soma2019 + soma2020 #total de visualizações do triênio
media_trienio = total_trienio / anotacoes_trienio #média de visualizações no triênio

#Obtendo as porcentagens de visualizações a que as visualizações de cada ano corresponde no triênio.

if total_trienio != 0: #não existe divisão por 0 nesse caso, sendo as porcentagens determinadas
    porcentagem2018 = (soma2018 / total_trienio) * 100
    porcentagem2019 = (soma2019 / total_trienio) * 100
    porcentagem2020 = (soma2020 / total_trienio) * 100
else: #divide-se por 0, logo as porcentagens serão indeterminadas
    porcentagem2018 = "indeterminada"
    porcentagem2019 = "indeterminada"
    porcentagem2020 = "indeterminada"

#Obtendo as médias de visualizações para cada ano do triênio (2018,2019 e 2020) e a média total do triênio
media2018 = (soma2018 / anotacoes_2018)
media2019 = (soma2019 / anotacoes_2019)
media2020 = (soma2020 / anotacoes_2020)
media_trienio = (visualizacoes_trienio / anotacoes_trienio)

#Imprimindo todos os dados que o problema pede
print("Canal:", canal)
print("Total de views do trienio:",visualizacoes_trienio)
print("Media de views do trienio:",format(media_trienio, ".2f"))
print("")
print("2018")
print("Total:",soma2018)
#Condicionando a impressão da porcentagem do ano de 2018 para que, se existir divisão por 0, será impresso indeterminada
if total_trienio != 0:
    print("Porcentagem das views do trienio:",format(porcentagem2018, ".2f"))
else:
    print("Porcentagem das views do trienio:",porcentagem2018)
print("Media:", format(media2018, ".2f"))
print("")
print("2019")
print("Total:",soma2019)
#Condicionando a impressão da porcentagem do ano de 2019 para que, se existir divisão por 0, será impresso indeterminada
if total_trienio != 0:
    print("Porcentagem das views do trienio:",format(porcentagem2019, ".2f"))
else:
    print("Porcentagem das views do trienio:",porcentagem2019)
print("Media:", format(media2019, ".2f"))
print("")
print("2020")
print("Total:",soma2020)
#Condicionando a impressão da porcentagem do ano de 2020 para que, se existir divisão por 0, será impresso indeterminada
if total_trienio != 0:
    print("Porcentagem das views do trienio:", format(porcentagem2020, ".2f"))
else:
    print("Porcentagem das views do trienio:", porcentagem2020)
print("Media:", format(media2020, ".2f"))