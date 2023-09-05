#Faça um programa para ler duas notas parciais, exibir a média parcial e dizer se o foi aprovado ou reprovado.

nota1 = round(float(input('Insira sua primeira nota: ')), 1)
nota2 = round(float(input('Insira sua segunda nota: ')), 1)
medianota = (nota1 + nota2) / 2

if(medianota == 10):
    print('Aprovado com distinção!')
elif(medianota >= 7):
    print('Aprovado por média. Média parcial: ', medianota)
else:
    print('Reprovado. Média parcial:', medianota)