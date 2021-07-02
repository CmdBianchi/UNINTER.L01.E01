###############################################################
#------------- > Exercicio 01 Lista:

x = float(input('Inserir dados ? 0 - Não && 1 - SIM \nDIGITE: '))
while (x == 1):
    name = input('Digite o nome do aluno: ')
    grade = float(input('Digite a nota do aluno: '))

    if(grade <= 2.9):
        status = 'E'
    elif(grade > 2.9) and (grade <= 4.9 ):
        status = 'D'
    elif (grade > 5.0) and (grade <= 6.9):
        status = 'C'
    elif (grade > 7.0) and (grade <= 8.9):
        status = 'B'
    else:
        status = 'A'
    print('-----------------------------------------------')
    print('O aluno {}, tirou a Nota {} e com o conceito {}.'.format(name, grade, status))
    print('-----------------------------------------------')
    x = float(input('Inserir dados ? 0 - Não && 1 - SIM \nDIGITE: '))
    print('')
print('PROGRAMA ENCERRADO......')