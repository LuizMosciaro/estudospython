#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

arquivo_download = float(input('Qual tamanho do arquivo de download? \n'))
velocidade = float(input('Qual sua velocidade de download? \n'))
tempo = arquivo_download/velocidade


print('O download teminará em ',str(tempo),'segundos')