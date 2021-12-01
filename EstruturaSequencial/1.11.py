#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

 #1   o produto do dobro do primeiro com metade do segundo .
 # 2  a soma do triplo do primeiro com o terceiro.
 #  3 o terceiro elevado ao cubo. 

x = float(input('Digite um número inteiro:'))
y = float(input('Digite o segundo número inteiro:'))
z = float(input('Digite um número real:'))

#1)
print('Baseado nos números que você colocou: \n')
resp1 = 'O produto do dobro de {0} com a metade de {1} é: {2}'
x1 = x*2
y1 = y*0.5
print(str(resp1.format(x,y,x1*y1)))

#2)
resp1 = 'A soma do triplo de {0} com {1} é: {2}'
x2 = x*3
print(str(resp1.format(x,z,x2+z)))

#3)
resp1 = 'O número {0} elevado ao cubo é {1}'
print(str(resp1.format(z,z**3)))

