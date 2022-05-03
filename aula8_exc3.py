km=float(input('Digite a quantidade de Km: '))
dias=float(input('Digite a quantidade de Dias: '))

dias=dias*60
km=km*0.015
total= km+dias

print('O valor de dias é R${} de kms é de R${} e o total do valor é {}'.format(dias,km,total))

