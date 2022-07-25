# Faça um programa que leia 5 números inteiros, adicione-os em uma lista e mostre-os.

numeros = []
print("Informe os 5 número interios:")
for i in range(5):
    numeros.append(input('numero ' + str(i+1) +':'))
    print(numeros)
