
idade=int(input('Idade: '))

novo=idade
velho=idade

while True:
    idade=int(input('Idade: '))
    if idade<0: 
        break
    
    if idade<novo:
        novo=idade
    elif idade>velho:
        velho=idade

media=(novo+velho)/2

print(f'Menor idade: {novo} \nMaior idade: {velho} \nMédia das duas idades: {media:.2f}')
