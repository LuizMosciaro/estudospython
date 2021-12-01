#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
import math

p1 = int(input('Quantos metros quadrados? \n'))
lata = 18
preco_lata = 80
litros_necessarios = p1/3


if litros_necessarios >= lata:
    latas = math.ceil(litros_necessarios/lata)
    print('Você precisará de ',round(litros_necessarios,2),' litros e necessitando comprar ',latas,'latas de tinta de 18 litros')
    print('O total será ',80*latas)
else:
    print('Precisará de apenas uma lata, total de R$80')
