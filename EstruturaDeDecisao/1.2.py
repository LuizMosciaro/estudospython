#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

a = float(input('Digite algum número: \n'))

if a >= 0:
    print('O número {} é positivo'.format(a))
else:
    print('O número {} é negativo'.format(a))