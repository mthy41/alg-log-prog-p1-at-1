salBruto = float(input('Insira seu salário: '))

if (salBruto <= 900):
    salLiq = salBruto
    desc = salLiq - salBruto
    desccent = 0
elif (salBruto <= 1500):
    salLiq = salBruto * 0.95
    desc = salBruto - salLiq
    desccent = 5
elif (salBruto <= 2500):
    salLiq = salBruto * 0.90
    desc = salBruto - salLiq
    desccent = 10
else:
    salLiq = salBruto * 0.80
    desc = salBruto - salLiq
    desccent = 20

salLiq = salLiq * 1.11 #Acréscimo do FGTS

salLiq = round(salLiq, 2)


print(f'Salário bruto: {salBruto}')
print(f'Desconto imposto de renda: -({desccent}%) {desc}')
print(f'FGTS (11%): +{round(salLiq - (salLiq * 0.89), 2)}')
print(f'Salário líquido {salLiq}')
    