#Faça um prograrama que peça um número maior que 1 ao usuário. Em seguida, imprima todos os números, de 1 até o número que o usuário informou.

num = int (input(' Digite um numero maior que 1: '))
ini = 1
while ini <= num:
    print(ini)
    ini += 1
else:
    print('Fim do while.')