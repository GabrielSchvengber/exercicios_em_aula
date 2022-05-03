print('''Após botar seu salário, digite seu cargo como:

1)Programador de Sistemas
2)Analista de sistemas
3)Analista de Banco de Dados

''')

cargo=float(input('Digite seu cargo: '))
salario=float(input('Digite seu salário: '))

if cargo == 1:
    aumento=salario+(salario*0.3)
    print('Seu salário será de:R${:.2f}'.format(aumento))
elif cargo == 2:
    aumento=salario+(salario*0.2)
    print('Seu salário será de :R${:.2f}'.format(aumento))
elif cargo == 3:
    aumento=salario+(salario*0.15)
    print('Seu salário será de:R${:.2f}'.format(aumento))
else:
    print('Cargo Inválido!')
