print('## Programa de empréstimos ## \n Responda: 0-Não e 1-Sim')
nomeNegativado= int(input('Possiu nome negativo? ' ))

if nomeNegativado == 1 :
   print('Não pode realizar o empréstimo.')
else:
     carteriraAssinada=int(input('Possui carteira assinada? '))
     if carteriraAssinada == 0:
        print('Não pode realizar o empréstimo')
     else:
          possuiCasaPropria = int(input('Possui casa própria? '))
          if possuiCasaPropria == 0:
             print('Não pode realizar o empréstimo.')
          else:
             print('Concede o empréstimo. ')
