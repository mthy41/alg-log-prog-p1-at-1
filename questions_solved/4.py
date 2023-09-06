#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = str(input('Digite uma letra (MAISÚCULA) '))

if (x=='A'or x=='E'or x=='I'or x=='O'or x=='U'):
    print('A letra é vogal.')
else:
    if (x=='Q'or x=='W'or x=='R'or x=='T'or x=='Y'or x=='P'or x=='S'or x=='D'or x=='F'or x=='G'or x=='H'or x=='J'or x=='K'or x=='L'or x=='Ç'or x=='Z'or x=='X'or x=='C'or x=='V'or x=='B'or x=='N'or x=='M'):
        print('A letra é uma consoante')
    else:
        print('Letra inválida')
