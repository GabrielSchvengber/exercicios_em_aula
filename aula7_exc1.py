
ano=int(input('Dgite um ano qualquer: '))

if ano%4==0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} Não é um ano bissexto'.format(ano))