#Faça um Programa que peça dois números e imprima o maior deles.

x = float(input('Insira um número '))
y = float(input('Insira outro número '))
x = int(x)
y = int (y)

if (x==y):
    print('Os números são iguais')
else:
    if (x > y):
        print(x)
    else:
        print(y)


