#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

a = float(input('Digite um numero 1: \n'))
b = float(input('Digite um numero 2: \n'))
c = float(input('Digite um numero 3: \n'))

lista = [a,b,c]
lista.sort(reverse = True) #o SORT() faz ficar em ordem crescente / com REVERSE=TRUE faz com que coloque a lista do menor para o maior numero


print(lista)
