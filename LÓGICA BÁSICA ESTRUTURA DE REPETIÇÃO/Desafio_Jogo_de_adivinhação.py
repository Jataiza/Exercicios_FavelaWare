from random import randint

tentativas = 5
jogador = input('Seu nome: ')

print('Olá %s vamos ver se você consegue adivinhar o número certo' % jogador)
print('Você tem %d tentativas\n' % tentativas)

print('Sorteando um número de 0 á 20...\nNúmero sorteado\nBoa sorte')

numero = randint(0, 20)


while (tentativas > 0):
    chute = input('Chute: ')
    tentativas -= 1

    if tentativas > 0:
        if int(chute) == numero:
            print('Meus parabéns %s você acertou!\n' % jogador)
            break
        elif int(chute) < numero:
            print('Você errou, agora tente um numero mais alto')
            print('Ainda lhe restam %d tentativas\n' % tentativas)
        elif int(chute) > numero:
            print('Você errou, agora tente um numero mais baixo')
            print('Ainda lhe restam %d tentativas\n' % tentativas)
    else:
        print('Infelizmente suas chances chegaram á zero %s, não foi dessa vez, mais sorte na proxima!' % jogador)
        print('O número certo era %d' % numero)