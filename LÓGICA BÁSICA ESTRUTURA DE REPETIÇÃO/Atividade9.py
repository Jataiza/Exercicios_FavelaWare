#Faça um programa em Python que leia n números inteiros e positivos a partir do teclado, até que o usuário digite 0. Ao final,
#informe o maior número digistado.

x = 'S'
cont = 0
maior = 0
menor = 0

while x != 'N':
    z = int(input('Digite um numero: '))
    cont += 1
    
    if cont == 1:
       maior = z
       menor = z
    else:
        if z > maior:
            maior = z
        if z < menor:
            menor = z
    
    x = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

print(f'O MAIOR número digitado foi {maior}.')
print(f'O MENOR número digitado foi {menor}.')