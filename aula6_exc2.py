velocidade=float(input('Qual velocidade você percorreu em Km/h? '))

if velocidade>80:
    multa = (velocidade - 80)*7
    print('Você passou da velocidade permitida. \nVocê recebeu uma multa de R${:.2f}'.format(multa))
else:
    print('Você não recebeu nenhuma multa. sua velocidade foi de {}'.format(velocidade))