lista=(int(input('Digite um número:')),int(input('Digite mais um número:')),int
(input('Digite outro número:')),int(input('Digite o ultimo número:')))

if 9 in lista:
    print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O número 3 foi digitado na {lista.index(3)+1} posição.')

for n in lista:
    if n%2==0:
        print( n, end=' ')    

