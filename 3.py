'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M -Masculino, Sexo Inválido.
'''
letra = str(input('Insira sua letra (MAÚSCULA) '))
fem = "F"
masc = "M"

if(letra == fem):
    print("Sexo feminino.")
else:
    if(letra == masc):
        print("Sexo masculino")
    else:
        print('Sexo inválido.')