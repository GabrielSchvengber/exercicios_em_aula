from random import randint

lista=('Pedra','Papel','Tesoura')

computador= randint(0,2)

perguntar=int(input('Digite a opção que você quer jogar: [0]Pedra [1]Papel [2]Tesoura :'))

print('O computador escolheu: {}'.format(lista[computador]))
print('O jogador escolheu: {}'.format(lista[perguntar]))

if computador == 0:
    if perguntar == 0:
        print('Empate')
    elif perguntar == 1:
        print('Jogador perdeu')
    elif perguntar == 2:
        print('Computador venceu')  
    else:
        print('Operação inválida')
elif computador == 2:
    if perguntar == 0:
        print('Jogador venceu')
    elif perguntar == 1:
        print('Computador venceu')
    elif perguntar == 2:
        print('Empate!')
    else:
        print('Operação inválida')
else:
    print('Operação invalida')
