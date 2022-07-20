#Escreva um prograrama que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 35%.


salario=float(input("Digite o seu sálario:"))

reajuste=salario + (salario*35 /100)

print("O valor do seu reajuste é:",reajuste)