
n1=0
n2=1

n=int(input('Digite um número: '))
print(f'{n1} {n2}',end=' - ')

for c in range(n-1):
    n3=n1+n2
    print(f'{n3}', end=' - ')

    n1=n2
    n2=n3
print('- Fim')
