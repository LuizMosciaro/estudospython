#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
#que calculará os reajustes.

#    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento. 

y = float(input('Qual seu salário atual? \n'))

if y <= 280:
    a = 0.2
    x = round(y*(1+a))
    print('Seu antigo salário era de ',y)
    print('Você ganhou um aumento equivalente a ',a*100,'%')
    print('Seu novo salário é de ',x,'!! ')

elif 280 <= y <= 700:
    a = 0.15
    x = round(y*(1+a))
    print('Seu antigo salário era de ',y)
    print('Você ganhou um aumento equivalente a ',a*100,'%')
    print('Seu novo salário é de ',x,'!! ')

elif 701 <= y <= 1500:
    a = 0.1
    x = round(y*(1+a))
    print('Seu antigo salário era de ',y)
    print('Você ganhou um aumento equivalente a ',a*100,'%')
    print('Seu novo salário é de ',x,'!! ')

elif 1501 <= y:
    a = 0.05
    x = round(y*(1+a))
    print('Seu antigo salário era de ',y)
    print('Você ganhou um aumento equivalente a ',a*100,'%')
    print('Seu novo salário é de ',x,'!! ')
