
print('Código de cargo: \n1 : Enfermeiro \n2 : Nutricionista \n3 : Médico(a)')

qtdenutri=0
totalSalNutri=0

while True:
    cargo = int(input('Informe um código de cargo: '))
    if cargo >= 1 and cargo <= 3:
        salario=float(input('Salário: '))
        if cargo == 2:
            qtdenutri += 1
            totalSalNutri+=salario
            
        resp=input('Deseja continuar [S/N] ')
        if resp.upper()=='N':
            break
    else:
        print('Cógido Inválido!')

if qtdenutri>0:
    media=totalSalNutri/qtdenutri
    print(f'Média de salário das nutricionistas {media:.2f}')

else:
    print('Não foram inseridos dados sobre nutricionistas')

    