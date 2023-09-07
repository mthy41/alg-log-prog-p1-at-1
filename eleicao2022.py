print('Candidatos disponíveis:\nJair M. Bolsonaro (22)\nLuiz Inácio Lula da Silva (22)\nCiro Gomes (15)')

voto = int(input('Insira seu voto: '))

if(voto == 22):
    result = "Luiz Inácio Lula da Silva"
elif(voto == 13):
    result = "Luiz Inácio Lula da Silva"
elif(voto == 15):
    result = "Voto nulo"
else:
    result = "Voto nulo"
    
print(f'O vencedor dessa eleição é: {result}.')