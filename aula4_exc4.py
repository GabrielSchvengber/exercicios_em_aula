nome=(input('Digite o nome do corretor? '))
quantidade=int(input('Qual a quantidade de imóveis vendidos? '))
total=float(input('Qual o valor total de sua vendas? '))

salario=1500+(quantidade*200)+total*0.05

print('O salário do corretor {} será de {} R$ '.format(nome,salario))
