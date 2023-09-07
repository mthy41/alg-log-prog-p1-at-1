import getpass

ver_bar = "----------------------------------"
vot_tab = "Candidatos\nJair M. Bolsonaro (22)\nLuis Inácio Lula da Silva (13)\nPablo Marçal (24)\nPinochet (60)\nAécio Neves (32)\nSergio Moro (92)"
hor_tab = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|"

vBol = 0
vLul = 0
vPm = 0
vPc = 0
vAe = 0
vSer = 0

nrep = 0 #nrep: número de repetições
vn = 0 #vn: número de iteração do loop (i)
maxrep = 20 #maxrep: número máximo de repetições

#loop pra pedir o nrep e checar e o número é valido
while (nrep <= 0):
  nrep = int(float(input(f'Número de pessoas que vão votar (max {maxrep}) ')))
  if (nrep <=0):
    print('Número inválido.')
    nrep = int(nrep)
    nrep = 0
  if (nrep >= maxrep):
    print('Número grande demais.')
    nrep = 0

#loop para criar senha
sen = "default"
versen = "default_ver"
print('Crie uma senha para ver os resultados')
while (sen != versen):
    sen = getpass.getpass('Nova senha:')
    versen = getpass.getpass('Verifique a senha')
    if (sen != versen):
        print("Senhas não batem, tente novamente.")
    else:
        print(hor_tab)


#loop para gerar as escolhas
while (vn < nrep):
    print(ver_bar)
    print(vot_tab)
    print('Insira seu voto: ')
    vt = int(input())
    input('Voto computado, pressione enter para o próximo.')
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
    vn = vn + 1

result = max(vBol, vLul, vPm, vPc, vAe, vSer)

if (sen != ""):
    print('Insira a senha para ver o resultado.')

endsen = ""
while (endsen != sen):
    endsen = getpass.getpass('Senha: ')
    if (endsen != sen):
        print('Senha incorreta, tente novamente.')


if ():
    print("Houve empate!")
elif (result == vBol):
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
    print("Ocorreu um erro na avaliação dos votos.")




