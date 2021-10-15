#Imprimir na tela Python Calculator
print('\033[1;30;45m-='*20, '\033[m', "\033[1;30;45mPYTHON CALCULATOR\033[m", '\033[1;30;45m-='*20, '\033[m')

#Entrada da escolha do usuário
cont = ' '
while cont != 'N':
    op = int(input('''Selecione o número da operação desejada: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite sua opção (1/2/3/4): '''))
    while op not in range(1,5):
        print('Valor inválido! Por favor, insira um valor válido.')
        op = int(input('''
Selecione o número da operação desejada: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite sua opção (1/2/3/4): '''))

    #Entrada dos dois números
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    #Funções que farão as operações
    if op == 1:
        soma = lambda num1, num2: num1+num2
        print(f'\n{num1} + {num2} = {soma(num1, num2)} ')
    elif op == 2:
        sub = lambda num1, num2: num1-num2
        print(f'\n{num1} - {num2} = {sub(num1, num2)} ')
    elif op == 3:
        mult = lambda num1, num2: num1*num2
        print(f'\n{num1} x {num2} = {mult(num1, num2)} ')
    elif op == 4:
        div = lambda num1, num2: num1/num2
        print(f'{num1} / {num2} = {div(num1, num2)}' )

    cont = str(input('\nDeseja continuar? (S/N): ')).upper()
