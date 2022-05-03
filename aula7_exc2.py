num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))
num3=int(input('Terceiro valor: '))


maior= num1
if( num2 > maior):
    maior=num2
if( num3 > maior):
    maior=num3

print('O número maior é: ', maior)

menor= num1
if(num2 < menor):
    menor=num2
if( num3 < menor):
    menor=num3

print('O menor número é: ', menor)