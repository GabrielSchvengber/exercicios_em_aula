salario=float(input('Escreva seu salário: '))

#maior=1250*0.10 (erro)
#menor=1250*0.15

#if salario==maior>1250 :
 #   print('Você obteve um aumento de: ', maior)

#else:
   # salario==menor<=1250 
  #  print('Você obteve um aumento de: ', menor)

if salario <=1250:
    novo=salario+(salario*0.15)
else:
    novo=salario+(salario*0.10)

print('Seu salário era de {} a passou a ser {}'.format(salario,novo))