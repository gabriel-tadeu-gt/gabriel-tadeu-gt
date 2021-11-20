#Criando as variáveis de entrada e convertendo a temperatura atual de Celsius para Fahrenheit
nome_do_material = input()
ponto_de_fusao = float(input())
ponto_de_ebulicao = float(input())
temperatura_fahrenheit = float(input())
temperatura_celsius = float((5 * (temperatura_fahrenheit - 32))) / 9 # Fórmula da física TC = (5 * (TF - 32)) / 9

#Ajustando casas decimais com round para usá-las nos cálculos/comparações:
ponto_de_fusao_formatado =  round(ponto_de_fusao, 2)
ponto_de_ebulicao_formatado = round(ponto_de_ebulicao, 2)
temperatura_celsius_formatada = round(temperatura_celsius, 2)

#Imprimindo os dados fornecidos:
print("Material:", nome_do_material)
# Usa-se format para adequar as casas decimais dos valores impressos
print("Ponto de fusao (Celsius):", format(ponto_de_fusao, '.2f')) 
print("Ponto de ebulicao (Celsius):", format(ponto_de_ebulicao, '.2f'))
print("Temperatura atual (Celsius):", format(temperatura_celsius, '.2f'))

#Definindo o estado físico da substância:
if temperatura_celsius_formatada < ponto_de_fusao_formatado:
    print("Estado fisico do material: Solido")
elif temperatura_celsius_formatada >= ponto_de_fusao_formatado and temperatura_celsius_formatada < ponto_de_ebulicao_formatado:
    print("Estado fisico do material: Liquido")
elif temperatura_celsius_formatada >= ponto_de_ebulicao_formatado:
    print("Estado fisico do material: Gasoso")