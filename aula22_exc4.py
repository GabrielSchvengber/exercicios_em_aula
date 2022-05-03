n = int(input('Digite um número impar maior que 1:'))

if n <=1 or n%2==0:
    print('Número informado não atende os critérios definidos.')
else:
    l = []
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero: '))
        l.append(num)#adiciona o valor na lista

centro=int(len(l)/2)
elementoCentro=l[centro]
fatorial=1#1*2*3*4*5=120(fatorial)

for n in range(2, elementoCentro+1):#começa no zero então '+1'
    fatorial*=n
print(f'Lista{l}')
print(f'O elemento do centro da lista {elementoCentro} e seu fatorial é igual a {fatorial}')
