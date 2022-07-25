#Faça um programa que leia 20 números inteiros e armazene-os em uma lista. Armazene os números pares na lista PAR e os 
# números ímpares na lista IMPAR. Imprima as três listas.

num = []
par = []
impar = []

for numero in range(0, 20):
    num.append(int(input("Digite um número: ")))

for numero in range(0, 20):
    if num[numero] % 2 == 0:
        par.append(num[numero])
    else:
        impar.append(num[numero])

print("num com 20 elementos: " + str(num))
print("num com elementos pares: " + str(par))
print("num com elementos impar: " + str(impar))