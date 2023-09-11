kgmor = float(input('Quantos kg(s) de morango deseja comprar?\n'))
kgmac = float(input('Quantos kg(s) de maçã deseja comprar?\n'))

if (kgmor <= 5):
    precmor = kgmor * 2.5
elif (kgmor > 5):
    precmor = kgmor * 2.2

if (kgmac <= 5):
    precmac = kgmac * 1.8
elif (kgmac > 5):
    precmac = kgmac * 1.5
    
if (((precmor + precmac) > 25) or (kgmor + kgmac > 8)):
    precfinal = (precmac + precmor) * 0.90
else:
    precfinal = precmac + precmor

print(f'Valor final: R$ {round(precfinal, 2)}')
