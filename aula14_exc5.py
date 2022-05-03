from random import randint

computador=randint(0,10)

print('Pensei em um némero de 0 á 10, tente adivinhar: ')

acertou=False
palpites=0

while not acertou:
    jogador=int(input('Qual seu palpite: '))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais...Tente mais uma vez')
        elif jogador>computador:
            print('Menos...Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns! '.format(palpites))
