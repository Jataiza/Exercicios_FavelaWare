#Faça um prograrama que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,mostrando uma
#mensagem de erro e voltando a pedir as informações.

nome= input("Digite nome de usuario: ")
senha = input(' Digite uma senha: ')
while senha == nome:
    print('nao pode')
    nome = input("Digite nome de usuario: ")
    senha = input(' Digite uma senha: ')
else:
    print("Usuário cadastrado com sucesso.")