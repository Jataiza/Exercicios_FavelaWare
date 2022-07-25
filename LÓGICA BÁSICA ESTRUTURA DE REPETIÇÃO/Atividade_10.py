#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número
#de caracteres).


nome = str(input("Informe o nome: "))
while (len(nome) <= 3) or (not nome.isalpha()):
    print("O nome deve ter mais que 3 caracteres e conter apenas letras.")
    nome = str(input("Informe o nome: "))


idade = int(input("Qual a idade? "))
while (idade < 0) or (idade > 150):
    print("A idade de ser entre 0 e 150.")
    idade = str(input("Informe uma idade válida: "))


salario = float(input("Informe o salário: "))
while (salario < 0):
    print("Valor inválido!")
    salario = float(input("Informe novamente um valor acima de 0 para o salário: "))


sexo = str(input("Informe o sexo (feminino ou masculino): ")).lower()
while (sexo != 'feminino') and (sexo != 'masculino') and (sexo != 'f') and (sexo !=  'm'):
    print("Informação inválida!")
    sexo = str(input("Informe o sexo (feminino ou masculino): "))


print("Informe S para solteiro(a), c para casado(a), v para viúvo(a) ou d para divorciado(a).")
e_civil = str(input("Informe o estado civil: ")).lower()

while (e_civil != 's') and (e_civil !='c') and (e_civil !='v') and (e_civil !='d'):
    print("Informação inválida! Informe S para solteiro(a), c para casado(a), v para viúvo(a) ou d para divorciado(a).")
    e_civil = str(input("Informe novamente o estado civil de acordo com a orientação acima: "))
