''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

maior=0
menor=100000
for c in range (0,5):
    peso=float(input('Informe seu peso: '))
    if peso>maior:
        maior = peso
    if peso<menor:
        menor = peso
print('Maior {:.2f}Kg e Menor {:.2f}Kg Peso'.format(maior,menor))
