###############################################################
#------------- > Exercicio 01 Lista:

x = float(input('Inserir dados ? 0 - Não && 1 - SIM \nDIGITE: '))
while (x == 1):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    if(nota <= 2.9):
        status = 'E'
    elif(nota > 2.9) and (nota <= 4.9 ):
        status = 'D'
    elif (nota > 5.0) and (nota <= 6.9):
        status = 'C'
    elif (nota > 7.0) and (nota <= 8.9):
        status = 'B'
    else:
        status = 'A'

    print('Nota {}, Nome {},  Conceito {}.'.format(nota, nome, status))
    x = float(input('Inserir dados ? 0 - Não && 1 - SIM \nDIGITE: '))