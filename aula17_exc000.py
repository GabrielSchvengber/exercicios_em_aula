frase=input('Digite uma frase: ')
caractere=input('Digite um caractere que busca:')

qtde:0

for c in frase: 
    if c.lower()==caractere.lower():
        qtde+=1

print(f'O caractere apareceu {qtde} na frase')
