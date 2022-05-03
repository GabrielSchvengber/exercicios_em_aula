#Converção de tupla em lista

'''dias=('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado')

semana=list(dias)#Troca de tupla para lista

print(f'A variavel semana é do tipo {type(semana)} e contém os dias da semana {dias}')'''

num=[]
for n in range(0,10):#numeros de 1 á 10 elevado ao quadrado
    num.append(n**2)
print(num)
# ou pra ser mais resumido
lista1=[x**2 for x in range(10)]
print(lista1)
#de 1 á 20 pegou apenas os números pares
lista2=[x for x in range(1,20) if x%2==0]
print(lista2)

lista3=[i for i in "HACKATHON" if i in ['A','E','I','O','U']]#inseringo vogais de uma string em uma lista
print(lista3)

lista4=[1,2,3]
lista4=[i**3 for i in lista4]#atribui novos valores aos elementos atravez de uma operação'faz o cubo dos números'
print(lista4)
