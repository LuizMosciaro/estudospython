#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 

p1 = input('Você é homem ou mulher? \nM = Mulher ou H = Homem ').upper()
a = float(input('Qual sua altura? '))


if p1 == 'H':
    peso_ideal_h = ((72.7*a)-58)
    print('Seu peso ideal é: ',round(peso_ideal_h))

if p1 == 'M':
    peso_ideal_m = ((62.1*a)-44.7)
    print('Seu peso ideal é: ',round(peso_ideal_m))



