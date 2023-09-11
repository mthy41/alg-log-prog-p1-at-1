gas = float(2.5)
alc = float(1.9)

combesc = input('Selecione o combustível:\nG para gasolina\nA para álcool.\n')
if(combesc == 'A' or combesc == 'a' or combesc == 'B' or combesc == 'b'):
    litrosesc= int(input('Insira a quantidade de litros:\n'))
    if (combesc == 'A' or combesc == 'a' and litrosesc <= 20):
        combval = (alc * 0.97) * litrosesc
        print(f'Valor total: R$ {round(combval,2)}')
    elif(combesc == 'A' or combesc == 'a' and litrosesc > 20):
        combval = (alc * 0.95) * litrosesc
        print(f'Valor total: R$ {round(combval,2)}')
    if(combesc == 'B' or combesc == 'b' and litrosesc <= 20):
        combval = (gas * 0.96) * litrosesc
        print(f'Valor total: R$ {round(combval,2)}')
    elif(combesc == 'B' or combesc == 'b' and litrosesc > 20):
        combval = (gas * 0.94) * litrosesc
        print(f'Valor total: R$ {round(combval,2)}')
else:
    print('Combustível inválido.')