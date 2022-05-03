frase=input('Escreva uma frase qualquer: ').upper().strip()

print('A)Quantidades de vezes que aparece a letra "A" são:{} '.format(frase.count('A')))

print('B)Em que posição aparece a primeira vez: {}'.format(frase.find('A')+1))

print('C)Em que posição aparece pela ultima vez: {}'.format(frase.rfind('A')+1))
