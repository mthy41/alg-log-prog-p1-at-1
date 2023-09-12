#Faça um Programa que leia um número inteiro menor que 1000 e imprima 
#a quantidade de centenas, dezenas e unidades do mesmo.

n1 = int(input('Insira um número'))
if (n1 > 1000 or n1 < 0):
    print("Número inválido")
else:
    cent = n1 // 100
    dez = (n1 % 100) // 10
    uni = n1 % 10
    print(f'Centenas: {cent}\nDezenas: {dez}\nUnidades: {uni}')