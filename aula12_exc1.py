cidade=str(input('Digite o nome de sua cidade: '))

n= cidade.split()
nome = 'santa'

if nome in cidade:
    print('Começa com "santa" sua cidade'.format(n[0]))
else:
    print('não começa com "santa" a sua cidade')