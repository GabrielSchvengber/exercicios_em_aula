from math import hypot

co=float(input('Qual o valor do cateto oposto? '))
ca=float(input('Qual o valor do cateto adjacente? '))

hi= hypot(co,ca)

print('O comprimento da hipotenusa é de:{:.2f} '.format(hi))
