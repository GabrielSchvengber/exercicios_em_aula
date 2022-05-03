print('1)á vista/cheque')#10% de desoconto
print('2)á vista no cartão')#5% de desc
print('3)em até 2x no cartão')#preco normal

pagamento=float(input('Digite sua forma de pagamento: '))

if pagamento == 1:
    valor=float(input('Digite o preço deste produto: '))
    desconto= valor - (valor*0.1)#(valor*10/100
    print('De R${} foi para R${}'.format(valor,desconto))
elif pagamento == 2:
    valor=float(input('Digite o preço deste produto: '))
    desconto= valor - (valor*0.05)
    print('De R${} foi para R${}'.format(valor,desconto))
elif pagamento == 3:
    valor=float(input('Digite o preço deste produto: '))
    print('R${} é o valor deste produto'.format(valor))
