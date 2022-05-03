
quantidade=float(input('Digite a quantidade de camisas: '))
valor=float(input('Informe o valor da camisas: '))

if quantidade <=5:
    quant=valor*quantidade
    desconto= quant - (valor*0.03)
    print('O valor da camisa {} e com desconto {:.2f}'.format(valor,desconto))
elif quantidade >=5 and quantidade <=10:
    quant=valor*quantidade
    desconto= quant - (valor*0.05)
    print('O valor da camisa {} e com desconto {:.2f}'.format(valor,desconto))
else:
    quant=valor*quantidade
    desconto=quant - (valor*0.07)
    print('O valor da camisa {} e com desconto {:.2f}'.format(valor,desconto))
    