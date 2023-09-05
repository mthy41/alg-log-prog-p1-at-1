#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Digite o número 1: '))
num2 = float(input('Digite o número 2: '))
num3 = float(input('Digite o número 3: '))

#Pior algoritmo impossível!!!
if(num1>num2>num3):
    print(f'O maior número é {num1} e o menor é {num3}')
elif(num1>num3>num2):
    print(f'O maior número é {num1} e o menor é {num2}')
elif(num2>num3>num1):
    print(f'O maior número é {num2} e o menor é {num1}')
elif(num2>num1>num3):
    print(f'O maior número é {num2} e o menor é {num3}')
elif(num3>num2>num1):
    print(f'O maior número é {num3} e o menor é {num1}')
elif(num3>num1>num2):
    print(f'O maior número é {num3} e o menor é {num2}')