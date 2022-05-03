primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão PA: '))
termo=primeiro
cont=1
while cont<=10:
    print(f'{termo}', end=' ')
    termo+=razao
    cont+=1
print('Fim!')
