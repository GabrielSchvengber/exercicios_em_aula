'''Construa um programa para fazer uma pequena entrevista com os alunos de uma turma. Na entrevista, são
informados o sexo e a idade de cada aluno. Considere que o usuário não sabe quantos alunos existem na turma.
O programa deve exibir a quantidade de homens acima de 18 anos e a quantidade de mulheres de qualquer idade.
Para encerrar o programa, o usuário deve informar uma idade negativa'''

mulheres=0
homens=0

while True:
    idade=int(input('Idade: '))
    if idade<0:
        break
    sexo=input('Sexo: ').upper()
    if sexo =='F':
        mulheres+=1
    elif sexo == 'M' and idade > 18:
        homens+=1
print(f'Total de mulheres {mulheres} e homens acima de 18 anos {homens}')
