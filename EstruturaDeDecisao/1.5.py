#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez. 

a = float(input('Digite sua nota 1: '))
b = float(input('Digite sua nota 2: '))

media = (a+b)/2

if media == 10:
    print('Aluno aprovado com honras')
elif media >= 7:
    print('Aluno aprovado')
elif media <= 7:
    print('Aluno reprovado')
