idade=float(input('Digite a sua idade: '))

falta= 18 - idade
passou= idade - 18

if idade > 18:
    print('Já passou {} anos da sua data de alistamento'.format(passou))
elif idade <= 18:
    print('Faltam {} anos para seu alistamento'.format(falta))
