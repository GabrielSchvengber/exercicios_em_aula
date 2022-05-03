num=int(input('Digite um número: '))
esc=int(input('Digite 1 se você quer o número binario, Digite 2 se você quer o número octal, Digite 3 se você que o número hexadecimal.: '))

if esc == 1 :
    print('O número {} binário fica: {}'.format(num,bin(num)))
elif esc == 2:
    print('O número {} octal fica: {}'.format(num,oct(num)))
elif esc == 3:
    print('O número {} hexadecimal fica: {}'.format(num,hex(num)))

