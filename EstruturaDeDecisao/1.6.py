#Faça um Programa que leia três números e mostre o maior deles. 

while True:
    try:
        a = float(input('Digite o primeiro numero: '))
        b = float(input('Digite o segundo numero: '))
        c = float(input('Digite o terceiro numero: '))
        maior = a

        if b > maior:
            maior = b
        elif c > maior:
            maior = c

        print('O maior numero é ',maior)

    except ValueError:
            print('Valor inserido é incorreto')
        