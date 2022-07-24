#Faça um programa que solicite a senha de um usuário e depois, peça para digitar novamente até que as duas senhas
#sejam correspondentes.

senha = input(' Digite uma senha: ')
conf = input(' Digite novamante a senha: ')

while senha != conf:
    print('nao pode')
    senha = input(' Digite uma senha: ')
    conf = input(' Digite novamante a senha: ')
else:
    print('senha cadrastada')