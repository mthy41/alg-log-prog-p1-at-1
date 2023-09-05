n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))

#Condição do isósceles
if (n2 == n1 and n1 != n3):
    print("O Triângulo é Isósceles")
elif (n1 == n3 and n1 != n2):
    print("O Triângulo é Isósceles")
elif (n2 == n3 and n1 != n2):
    print("O Triângulo é Isósceles")
elif (n1 == n2 == n3):
    print ("O Triângulo é Equilátero")
elif (n1 != n2 != n3):
    print("O Triângulo é Escaleno")