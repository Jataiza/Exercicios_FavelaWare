#Faça um prograrama em Python que leia n números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre a
#soma de todos os números digitados.

soma = 0
quantidade = 0
while True:
    n = int(input("Digite números inteiros para sair do loop digite 0: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")