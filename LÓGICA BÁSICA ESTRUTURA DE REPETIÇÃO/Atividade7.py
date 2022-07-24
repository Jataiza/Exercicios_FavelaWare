#Faça um programa que peĀue 10 idades menores que 100 e faça
#a média das idades, se o usuário inserir idade maior que 100
#repita até que seja inserido um número válido. (CORRIGIR)

pessoas = 0
i = 0
soma = 0

while i < len(pessoas):
    pessoas[i] = int(input("Digite a sua idade: "))
    soma = soma + pessoas[i]
    i = i + 1

i = 0
soma = 0

while i < len(pessoas):

    pessoas = pessoas[i]
    pessoas = int(pessoas)

    soma = soma + pessoas
    i = i + 1
print(soma)