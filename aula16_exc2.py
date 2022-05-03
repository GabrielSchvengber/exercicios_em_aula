'''Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o
usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do medicamento
mais barato, bem como a média aritmética dos preços informados'''


soma=0

nome=input('Digite o nome do Medicamento: ')
valor=int(input('Digite o valor do Medicamento:R$ '))

maisBarato=nome
menorPreco=valor

soma+=valor

for x in range(4):
    nome=input('Medicamento: ')
    valor=float(input('R$: '))
    soma+=valor
    if valor < menorPreco:
        menorPreco=valor 
        maisBarato=nome
    soma+=valor
media=soma/5

print('O medicamento mais barato é o {} que custa R${} e a média de valores são {}R$'.format(maisBarato,menorPreco,media))
