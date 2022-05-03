from random import randint

computador=randint(0,5)

print('Vou pensar num número de 0 á 5 tente adivinhar')
jogador=int(input('Em qual número estou pensando? '))

if jogador == computador:
    print('Você Acertou')
else:
    print('Você Errou! eu escolhi o número {}'.format(computador))
