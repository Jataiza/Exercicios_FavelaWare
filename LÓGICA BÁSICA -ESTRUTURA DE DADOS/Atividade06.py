# Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, em seu programa o usuário deverá inserir
# uma sequência de valores que representam a temperatura em graus Fahrenheit, seu programa deve
# receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco (uma
# string vazia). Converta todos os valores presentes na lista
# para graus Celsius e imprima na tela em uma formatação amigável ao usuário.
lista= list()
quantTemp= int(input("informe a quantidade de temperaturas a serem digitadas"))
i=0
graus=0.0
ii=0
while quantTemp > i:
    
    lista.append(float(input("escreva temperatura")))
    i+=1
    
else:
    print(lista)
while lista != ii:
    graus =(lista[ii]-32)* (5/9)
    print (graus)
    ii+=1


