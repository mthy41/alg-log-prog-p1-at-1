n1 = int(input('Insira o número 1\n'))
n2 = int(input('Insira o número 2\n'))
n3 = int(input('Insira o número 3\n'))

first = max(n1, n2, n3)
middle = min(n1, n2, n3)
last = min(n1, n2, n3)

if(n1 != last and n1 != first):
    middle = n1
if(n2 != last and n2 != first):
    middle = n2
if(n3 != last and n3 != first):
    middle = n3

print(first, middle, last)