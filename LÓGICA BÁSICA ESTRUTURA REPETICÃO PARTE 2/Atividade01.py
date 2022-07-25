#Faça um programa que gere a tabuada de qualquer número inteiro de 1 a 10. O usuário deve inÿormar de qual número ele
#quer ver a tabuada. A saída deve ser conforme o exemplo abaixo:

tabuada=int(input("Digite um  numero pra exibir a tabuada:"))
print("A tabuada do número",tabuada)

for valor in range (1,11,1):
    print(str(tabuada)+"x"+str(valor)+"="+str((tabuada*valor)))