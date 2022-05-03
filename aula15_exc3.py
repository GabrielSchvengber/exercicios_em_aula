'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 1) a
média de idade do grupo. 2) qual é o nome do homem mais velho. 3) quantas mulheres têm menos de 20 anos'''

somaIdade= 0 
maiorIdadeHomem=0
nomemaisvelho= ''
mulhermenor=0
mediaidade=0

for p in range(1,5):
    nome=input('Nome ').strip()
    idade=int(input('Idade '))
    sexo=input('Sexo [F/M] ').strip().upper()

    somaIdade+=idade

    if p==1 and sexo in 'M':
        maiorIdadeHomem=idade
        nomemaisvelho=nome
    if sexo in 'M' and idade>maiorIdadeHomem:
        maiorIdadeHomem=idade
        nomemaisvelho=nome
    if sexo in 'F' and idade<20:
        mulhermenor+=1

mediaidade=somaIdade/4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomemaisvelho))
print('Ao todo serão {} mulheres com menos de 20 anos'.format(mulhermenor))
