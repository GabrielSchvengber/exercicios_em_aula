'''frase=input('Digite uma frase: ').strip().upper() #Apos a sopa

palavras=frase.split() #apos a sopa
junto=''.join(palavras)#aposasopa
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]

if inverso==junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo')'''

frase=input('Digite uma frase: ').strip().upper() #Apos a sopa

palavras=frase.split() #apos a sopa
junto=''.join(palavras)#aposasopa
inverso=junto[::-1]
print(f'O invérso de {junto} é {inverso}')
if inverso==junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo')
