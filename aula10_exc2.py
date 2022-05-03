r1=float(input('Primeiro segmento: '))
r2=float(input(' Segundo segmento: '))
r3=float(input('Terceiro segmento: '))

#if r1+r2<r3 and r2+r1<r2 and r3+r1<r2:
 #   print('Os segmentos acima  NÂO PODEM formar um triangulo')
#elif (r1==r2) and (r1==r3):
 #   print('é um triangulo Equilátero')
#elif (r1==r2) or (r1==r3) or (r2==r3):
 #   print('é um triangulo Esóceles')
#else:
 #   print('é um triangulo Escaleno')
if r1<r2+r3 and r2<r1 and r3<r1+r2:
    print('Os segmentos PODEM formar um triangulo.')
    if r1==r2 and r2==r3 and r3==r1:
        print('Equilatero')
    elif r1!=r2 and r1!=r3 and r2!=r1:
        print('Escaleno')
    else:
        print('Isóseles')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')