#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#   1-Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde 
#   os valores para cima, isto é, considere latas cheias. 
import math

area = int(input('Quantos metros quadrados? \n'))
lata = 18
preco_lata = 80
galao = 3.6
preco_galao = 25
litros_necessarios = area/6

#usando só latas
latas = round(litros_necessarios/lata)

#usando só galoes
galoes = round(litros_necessarios/galao)

#misturando a melhor combinação de latas+galoes
mix = (litros_necessarios/lata)
mix_lt_gl = (litros_necessarios%latas/3.6)



print('Você pode comprar ',latas,' lata(s) de 18L, ou ',galoes,'galoes de 3.6L')
print('Também pode misturar ',mix,' latas com ',mix_lt_gl,' galoes')

