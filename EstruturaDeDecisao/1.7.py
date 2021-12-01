#Faça um Programa que leia três números e mostre o maior e o menor deles. 

a = float(input('Digite um numero 1: \n'))
b = float(input('Digite um numero 2: \n'))
c = float(input('Digite um numero 3: \n'))

#calculando o maior
maior = a   
if b > maior:
    maior = b
if c > maior:
    maior = c

#calculando o menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c


print('O maior número é o {} e o menor é o {}'.format(maior,menor))