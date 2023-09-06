#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

x = float(input('Digite um número '))
x = int(x)

if (x == 0):
    print("O número é igual a zero")
else:
    if (x > 0):
        print("O número é positivo.")
    else:
        print("O número é negativo.")