sal = float(input('Digite seu salário:\n'))
aumsal = 0
salaum = 0



if(sal <= 0):
    print('Salário inválido.')
elif(sal > 0 and sal <= 280):
    aumsal = 1.20
    salaum = sal * aumsal
    salaum = round(salaum, 2)
    print(f'O seu salário era: R$ {sal}\nAumentou: {int((100*aumsal)-100)}%\nSalário atual com aumento: R$ {salaum}')
elif(sal >= 281 and sal <= 700):
    aumsal = 1.15
    salaum = sal * aumsal
    salaum = round(salaum, 2)
    print(f'O seu salário era: R$ {sal}\nAumentou: {int((100*aumsal)-100)}%\nSalário atual com aumento: R$ {salaum}')
elif(sal >= 701 and sal <= 1499):
    aumsal = 1.1
    salaum = sal * aumsal
    salaum = round(salaum, 2)
    print(f'O seu salário era: R$ {sal}\nAumentou: {int((100*aumsal)-100)}%\nSalário atual com aumento: R$ {salaum}')
elif(sal >= 1500):
    aumsal = 1.05
    salaum = sal * aumsal
    salaum = round(salaum, 2)
    print(f'O seu salário era: R$ {sal}\nAumentou: {int((100*aumsal)-100)}%\nSalário atual com aumento: R$ {salaum}')

    