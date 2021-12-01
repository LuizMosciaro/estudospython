#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês. 

salario_hr = float(input('Quanto você ganha por hora?'))
horas_trab = float(input('Quantas horas trabalha no mês?'))


salario = salario_hr*horas_trab

print('Seu salário mensal é',salario,'reais')