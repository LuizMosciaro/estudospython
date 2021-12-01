#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#    salário bruto.
#    quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#    o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#   + Salário Bruto : R$
#    - IR (11%) : R$
#    - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#    = Salário Liquido : R$

salario_hr = float(input('Qual seu pagamento por hora? \n'))
horas_trab = float(input('Quantas horas trabalhadas no mês? \n'))
salario_bruto = salario_hr*horas_trab

IR = salario_bruto*0.11
INSS = salario_bruto*0.08
sind = salario_bruto*0.05
salario_liq = salario_bruto-IR-INSS-sind

print('____________________')
print('Seu ganho total no mês é de R$',salario_bruto)
print('____________________')
print('Descontos \n____________________')
print('Desconto de IR: ',IR)
print('Desconto de INSS: ',INSS)
print('Desconto do Sindicato: ',sind)
print('Salário Líquido: ',round(salario_liq,5))