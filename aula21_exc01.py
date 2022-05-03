lista= [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
maiorvalor=lista[0]
menorvalor=lista[0]
listaPares=[]
ocorrencia=0
mediaElementos=0
somaNegativo=0

for index in range(0,len(lista)):
    #maior valor
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]#percorrer todas posições e ver o mair elemento
    #menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #lista de numeros pares
    if lista[index]%2==0:
        listaPares.append(lista[index])#lista recebe o valor 12 listaPares=[12,...]
    #ocorrencia primeiro elemento
    if lista[index]==lista[0]:
        ocorrencia+=1
    #somatório para a média
    mediaElementos+=lista[index]
    #soma para numeros negativos
    if lista[index]<0:
        somaNegativo+=lista[index]
#media
mediaElementos/=len(lista)

print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listaPares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média de elementos: {mediaElementos}')
print(f'Elemetos negativos: {somaNegativo}')
