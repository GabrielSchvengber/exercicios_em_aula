from math import sqrt

lista=[9,3,5,7,2,1]

menor=min(lista)#menor
maior=max(lista)#maior
media_geo=sqrt(menor*maior)#media= menor*maior

print(f'Lista: {lista}')
print(f'Médio geométrica entre {menor} e {maior} é igual a {media_geo}')
