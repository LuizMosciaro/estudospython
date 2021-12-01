#Faça um Programa que peça dois números e imprima o maior deles. 

a = int(input('Digite algum número: \n'))
b = int(input('Digite um segundo número: \n'))

while True:
    if a > b:
        print('O maior número é ',a)
        
    else:
        print('O maior número é ',b)
        