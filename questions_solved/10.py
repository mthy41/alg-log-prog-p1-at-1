print('Selecione o turno em que você estuda:\nM para matutino;\nT para vespertino (tarde);\nN para noturno')
turno = str(input())
if(turno == 'M' or turno == 'm'or turno == 'T' or turno == 't' or turno == 'N' or turno == 'n'):
    if(turno == 'M' or turno == 'm'):
        print('Bom dia!')
    elif(turno == 'T' or turno == 't'):
        print('Boa tarde!')
    elif(turno == 'N' or turno == 'n'):
        print('Boa noite!')
else:
    print('Turno inválido.')