#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

a = input('Qual horário você estuda? \n M = Matutino \n V = Vespertino \n N = Noturno \n').upper()

if a == 'M':
    print('Bom dia!')

elif a == 'V':
    print('Boa tarde!')

elif a == 'N':
    print('Boa noite!')

else:
    print('Valor inválido..')