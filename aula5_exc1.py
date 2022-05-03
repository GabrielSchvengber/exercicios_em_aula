from math import trunc

num=float(input('Digite um valor: ')) #entrar no math   #quando colocar um numero de (,) troque por (.)
porcao = trunc (num)

print('O valor digitado foi {} e sua porção inteira é {}'.format(num,porcao))
