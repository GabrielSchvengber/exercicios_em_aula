''' Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para
validar o seu acesso ao sistema. Considere que a senha fictícia do correntista é 123456. Considere as seguintes
restrições: a) quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja bem-vindo ao nosso
banco!" b) quando o usuário errar a senha pela primeira vez, mostrar a mensagem: “Senha incorreta! Você ainda
tem 2 tentativas.” c) se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha incorreta! Você
ainda tem 1 tentativa.” d) se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi bloqueada!
Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado.'''

tentativa=2
stop=False
while not stop :
    nome=input('Digite seu nome: ')
    senha=int(input('Digite sua senha: '))
    if senha != 123456 and tentativa == 2:
        tentativa-=1
        print('A senha está incorreta! Você tem mais duas tentativas')
    elif senha != 123456 and tentativa == 1:
        tentativa-=1
        print('A senha está incorreta! Você tem mais 1 tentativas')
    elif senha != 123456 and  tentativa == 0:
        stop=True
        tentativa-=1
        print('Sua senha foi bloqueada!')
    elif senha == 123456:
        stop=True
        print('Olá {}. Seja bem-vindo ao nosso banco!'.format((nome)))
        

'''for c  in range(3,0,-1):
    senha = int(input('Senha: '))
    if senha == 123456:
        print('Olá, seja bem-vindo ao nosso banco!')
        break
    elif senha != 123456:
        print('Senha incorreta você tem {} tentativa(s)'.format(c-1))
        if c==1:
            print('Sua senha foi bloqueada!Por favor se dirija a algum de nossos caixas.')
            break'''
