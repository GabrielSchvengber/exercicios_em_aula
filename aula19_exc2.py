
num=0
soma=0
quant=0

num=int(input('Digite um número ou 999 para parar: '))

while num!=999:
    
    soma+=num
    quant+=1
    num=int(input('Digite um número ou 999 para parar: '))

print(f'Quantidade {quant} e soma {soma}')
