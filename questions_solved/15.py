#apenas com operador lógico or
l1 = float(input('Insira o lado 1 do triângulo: '))
l2 = float(input('Insira o lado 2 do triângulo: '))
l3 = float(input('Insira o lado 3 do triângulo: '))

if (l1 <= 0 or l2 <= 0 or l3 <= 0):
    print('O triângulo não possui lado(s) válido(s).')
elif (l1 == l2 == l3):
        print('O triângulo é Equilátero')
elif(l1 == l2 or l1 == l3 or l2 == l3):
        print('O triângulo é Isósceles.')
elif(l1 != l2 != l3):
        print('O triângulo é Escaleno.')
        
#apenas com operador lógico and
'''n1 = int(input('Insira o lado 1 do triângulo: '))
n2 = int(input('Insira o lado 2 do triângulo: '))
n3 = int(input('Insira o lado 3 do triângulo: '))

if (n2 == n1 and n1 != n3):
    print("O Triângulo é Isósceles")
elif (n1 == n3 and n1 != n2):
    print("O Triângulo é Isósceles")
elif (n2 == n3 and n1 != n2):
    print("O Triângulo é Isósceles")
elif (n1 == n2 == n3):
    print ("O Triângulo é Equilátero")
elif (n1 != n2 != n3):
    print("O Triângulo é Escaleno")'''
