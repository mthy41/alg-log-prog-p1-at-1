#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitaroutro valor deve aparecer valor inválido.

dia = int(input('Insira o número da semana: '))

if(dia == 1):
    print('O dia é Domingo.')
elif(dia == 2):
    print('O dia é Segunda.')
elif(dia == 3):
    print('O dia é Terça-Feira.')
elif(dia == 4):
    print('O dia é Quarta-Feira.')
elif(dia == 5):
    print('O dia é Quinta-Feira.')
elif(dia == 6):
    print('O dia é Sexta-Feira.')
elif(dia == 7):
    print('O dia é Sábado.')
else:
    print('Número da semana inválido.')