#lista = ['José','Janaina','Maria','Carlos']
#listaa = ['José','Pedro']

#for n in range(0, len(lista)):#Somente exibir os nomes

#lista.append('Jorge')#Ultimo da lista

#lista.insert(0, 'Jorge')#Primeiro da lista

#lista.sort()#Ordenar do menor para o maior(alfabético)

#lista.sort(reverse=True)#Ordenar do maior para o menor

#del lista[-1]#Remova o ultimo elemento 

#lista.remove('Janaina')#Remove janaina

#lista.pop()#Se nao passar nenhum parametro dentro do () ele remove um aleatório

#lista.clear()#Limpa a lista tiranod tudo

#listaa=lista#Deixa uma lista sempre igual a outra(mesmo se alterar algo em uma automaticamente muda na outra)

#listaa=lista[:]#'[:]'faz com que somente ela seja alterada

#lista.append('José')#Adiciona o nome

    #lista.extend(listaa)#Adiciona uma lista em cima da outra

#print(lista.count('José'))#Procura quantas vezes a palavra aparece dentro da lista

#print(len(lista))#Ver quantos nomes tem na lista

#print(lista.index('Janaina'))#Mostra a posição de janaina dentro da lista

'''for indice, nome in enumerate(lista):
    print(f'{nome} está armazenado no índice {indice}')#Mostra o nome e onde se localiza o índice'''
#a=[[2,1,-5],[3,7,0],[6,4,8]]#lista


#print(a[0][2])#o primeiro [] mostra a as caixas o segundo [] mostra qual posição
#print(a[0][0]+a[0][1]+a[0][2])#faz a soma das casas
#print(a[0][0],a[0][1],a[0][2])

#soma_a = 0
#lin = len(a)# 1  2  3 casas
#col = len(a[0])# com 1 2 3 elementos dentro

#for  i  in range(lin):
    #for j in range(col):
        #soma_a += a[i][j]
#print(soma_a)#Somou todos elementos dentro das casas