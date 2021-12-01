#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

a = input('Digite F para Feminino ou M para Masculino: \n').upper()

if a == 'F':
    print('Você escolheu Feminino.')

elif a == 'M':
    print('Você escolheu Masculino.')

else:
    print('Escolha inválida.')