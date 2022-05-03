#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progressão


p=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão deste termo: '))

decimo_termo= p +(9*r)

for c in range (p,decimo_termo +r, r):
    print('{}'.format(c), end='-')
print('Fim!')
