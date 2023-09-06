print("Vamos fazer te fazer algumas perguntas \nResponda com S para sim ou N para não.")

#qp é o número de pontos
qp = 0

q1 = str(input('Telefonou para a vítima? '))
if (q1 == 'S'):
    qp = qp + 1
    
q2 = str(input('Esteve no local de fuga? '))
if (q2 == 'S'):
    qp = qp + 1
    
q3 = str(input('Mora perto da vítima? '))
if (q3 == 'S'):
    qp = qp + 1
    
q4 = str(input('Devia para a vítima? '))
if (q4 == 'S'):
    qp = qp + 1
    
q5 = str(input('Já trabalhou para a vítima? '))
if (q5 == 'S'):
    qp = qp + 1

if (qp == 0):
    print('Inocente')
elif (qp == 2):
    print("Supeita")
elif (3 <= qp >= 4):
    print("Cúmplice")
else:
    print("Assasino")

print(qp)
