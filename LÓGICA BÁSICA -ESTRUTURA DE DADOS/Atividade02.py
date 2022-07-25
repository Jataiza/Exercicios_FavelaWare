#Faça um programa que leia 10 números reais, adicione-os em uma lista e mostre-os na ordem inversa.

numeros = []
print("Informe os 10 número interios:")
for i in range(10):
    numeros.append(float(input('Numero ' + str(i+1) + ':\n')))
    numeros.reverse()
    print(numeros)
