p1 = round(float(input('Insira o preço do produto 1: ')),2)
p2 = round(float(input('Insira o preço do produto 2: ')),2)
p3 = round(float(input('Insira o preço do produto 3: ')),2)

pb = min(p1, p2, p3)

print(f'Você deve comprar o produto que vale R$ {pb}!!')