#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

if(dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano > 0):
    print(f"Data válida. {ano}/{mes}/{dia}")
else:
    print(f'Data inválida.')