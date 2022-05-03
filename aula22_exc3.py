''' Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua
cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que compraram a
rifa. Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.'''
from random import shuffle,choice

rifa=[]#cria uma lista

while True:
    cadastro=input("Digite seu nome: ")
    rifa.append(cadastro)#adiciona o nome na lista
    resp=input('Deseja continuar [S/N]')
    if resp.upper()=='N':#se digitar 'n' encerra
        break
    
shuffle(rifa)
sorteado=choice(rifa)

print(f'Quem ganha o prêmio é {sorteado}')
