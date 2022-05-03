'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores'''

maior=0
menor=0

for c in range (0,7):
    nas=int(input('Informe seu ano de nascimento: '))
    data=2022-nas
    if data>=18:
        maior+=1
    else:
        menor+=1
print('Tem {} menores e {} maiores que 18 anos'.format(menor,maior))
        