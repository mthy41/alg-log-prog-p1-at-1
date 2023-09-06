#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
#de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
nm = (n1 + n2) / 2
nm = round(nm, 2)

if(n1 < 0 or n2 < 0):
    print('Nota(s) atribuída(s) inválida(s).')
elif(nm >= 0 and nm <= 4):
    print(f'Sua média Parcial é {nm}\nConceito: E\nREPROVADO')
elif(nm > 4 and nm <= 6):
    print(f'Sua média Parcial é {nm}\nConceito: D\nREPROVADO')
elif(nm > 6 and nm <= 7.5):
    print(f'Sua média Parcial é {nm}\nConceito: C\nAPROVADO')
elif(nm >7.5 and nm <= 9):
    print(f'Sua média Parcial é {nm}\nConceito: B\nAPROVADO')
elif(nm > 9 and nm <= 10):
    print(f'Sua média Parcial é {nm}\nConceito: A\nAPROVADO')