ver_bar = "----------------------------------"
vot_tab = "Candidatos\nJair M. Bolsonaro (22)\nLuis Inácio Lula da Silva (13)\nPablo Marçal (24)\nPinochet (60)\nAécio Neves (32)\nSergio Moro (92)"
hor_tab = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|"

vBol = 0
vLul = 0
vPm = 0
vPc = 0
vAe = 0
vSer = 0

i = 1
while (i < 4):
    print(ver_bar)
    print(vot_tab)
    print('Insira seu voto: ')
    vt = int(input())
    print(hor_tab)
    if (vt == 22):
        vBol = vBol + 1
    elif (vt == 13):
        vLul = vLul + 1
    elif (vt == 24):
        vPm = vPm + 1
    elif (vt == 60):
        vPc = vPc + 1
    elif (vt == 32):
        vAe = vAe + 1
    elif (vt == 92):
        vSer = vSer + 1
    else:
        print('Número de votação inválido, seu voto foi anulado.')
        input('Pressione enter para continuar.')
        print(hor_tab)
    i = i + 1

result = max(vBol, vLul, vPm, vPc, vAe, vSer)

if (result == vBol):
    print("O candidato vencedor é Jair M. Bolsonaro!")
elif (result == vLul):
    print("O candidato vencedor é Luiz Inácio Lula da Silva!")
elif (result == vPm):
    print("O candidato vencedor é Pablo Marçal!")
elif (result == vPc):
    print("O candidato vencedor é Pinochet!")
elif (result == vAe):
    print("O candidato vencedor é Aecio Neves!")
elif (result == vSer):
    print("O candidato vencedor é Sergio Moro!")
else:
    print("Ocorreu um erro na avaliação dos votos. :(")




