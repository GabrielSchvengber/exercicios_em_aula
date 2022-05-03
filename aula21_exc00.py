'''dias=('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')#tuple

print(type(dias))

print(dias[3])#printar quarta'''

'''texto='python'
tuple(texto)#tupla não muda enquanto uma lista pode ser alterada igual no ex abaixo
print(tuple(texto)) #separando 'python' por letras'''

'''lista=[1,2,3,4,]
lista[2]=8#faz a substituição do 2 para o 8
print(tuple(lista))'''

'''lista=[3,5]
tupla1=(1,2,lista)
tupla2=(1,2,lista[0],lista[1])#valores dentro da lista

#print(tupla)

#print(tupla[2])

#print(len(tupla2)) 

print(tupla2.count(2))

lista=['python', 1, 2,'java']
print(lista)'''

'''meses= ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n=1
while n<4:
    mes=int(input('Escolha um mês [1-12]: '))
    if 1<=mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1'''

#meses= ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

#print(meses[:3])#ate o terceiro

#print(meses[4:])# a partir de quatro

#print(meses[-3:])#somente os três ultimos

#meses.append('janaina')

#print(meses)#adiciona um item a mais 'janaina'(só funciona em lista)(somente um elemento por vez)

#meses+=['janaina','zé']#nesse método pode adicionar dois por vez
#print(meses)

#for mes in meses:#um abaixo do outro
 #   print(mes, end=' ')#end deixa um do lado do outro
