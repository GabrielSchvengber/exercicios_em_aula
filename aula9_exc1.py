
casaValor=float(input('Digite o valor da Casa: '))
salario=float(input('Digite o salário do comprador: '))
anos=float(input('Digite em quantos anos ele vai pagar: '))

#a prestação mensal não pode passsar de 30% do salario ou o empréstimo será negado

meses = anos *12                    #um ano tem 12 meses
prestacao= casaValor/meses

if prestacao > salario*0.3:             #30% do salário
    print('Impréstimo negado, a prestação passou de 30%')
else:
    print('Seu empréstimo foi aceito, com R$:{} de mensalidade.'.format(prestacao))