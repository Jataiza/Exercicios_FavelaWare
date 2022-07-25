# Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, em seu programa o usuário deverá inserir
# uma sequência de valores que representam a temperatura em graus Fahrenheit, seu programa deve
# receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco (uma
# string vazia). Converta todos os valores presentes na lista
# para graus Celsius e imprima na tela em uma formatação amigável ao usuário.
def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()



