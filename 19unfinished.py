#Faça um Programa que leia um número inteiro menor que 1000 e imprima 
#a quantidade de centenas, dezenas e unidades do mesmo.

n1 = int(input('Insira um número'))
if (n1 > 1000):
    print("Número inválido, insira um número menor da próxima vez.")
else:
    n1 = len(str(n1))
print(n1)