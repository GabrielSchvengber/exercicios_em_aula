#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

n = int(input('Digite um número para saber a tabuada: '))  
for c in range(1,11):
  print('{} x {} = {}'.format(n,c,n*c))
