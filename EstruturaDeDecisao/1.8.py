#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.

a = float(input('Qual preço da maçã?\n '))
b = float(input('Qual preço da banana?\n '))
c = float(input('Qual preço da laranja?\n '))

if a < b and a < c:
    print('A maça é mais barata')
elif b < a and b < c:
    print('A banana é mais barata')
elif c < b and c < a:
    print('A laranja é mais barata')
elif c == a or c == b or a == b:
    print('Há preços iguais, pode escolher')
