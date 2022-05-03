#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
#esteja errado, peça a digitação novamente até ter um valor correto.

sexo=str(input('Digite seu sexo: [M/F]')) .strip().upper()       #trip=tirar espeços, upper=deixa tudo maiusculo
while sexo not in 'MF':
    print(' Você não digitou M ou F! ')
    sexo=str(input('Dados inválidos, Digite seu sexo: [M/F]')).strip().upper()
print('Sexo {} resgistrado com sucesso!!'.format(sexo))
