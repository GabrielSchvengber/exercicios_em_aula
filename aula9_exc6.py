menu=int(input('\n ********************************************* \n CÁLCULO DAS GRANDEZAS ELÉTRICAS \n ********************************************* \n 1. Tensão (em Volt) \n 2. Resistência (em 0hm) \n 3.Corrente (em Ampéres) \n ********************************************* \n 1)Tensão 2)Resistência 3)Correntes:'))


if menu< 1 or menu>3:
    print('Opção Inválida')
elif menu == 1:
    vamo1=int(input('Digite o valor da Resistência: '))
    vamo2=int(input('Digite o valor da Corrente: '))
    U=vamo1*vamo2
    print('O valor da tensão será de {} Volt'.format(U))
elif menu == 2:
    vamo1=int(input('Digite o valor da Tensão: '))
    vamo2=int(input('Digite o valor da Corrente: '))
    R=vamo1/vamo2
    print('O valor da resistencia será de {} hm.'.format(R))
elif menu == 3:
    vamo1=int(input('Digite o valor da Tensão: '))
    vamo2=int(input('Digite o valor da Resistência: '))
    I=vamo1/vamo2
    print('O valor da corrente será de {} Ampére'.format(I))
