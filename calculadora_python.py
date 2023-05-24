'''
Calculadora básica utilizando looping em while
'''
print('****Calculadora****')

while True: #looping iniciado
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    operador = input('Digite qual operador irá utilizar. "+ - / *": ')
    
    numero1_float = 0
    numero2_float = 0
    numero_valido = None
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print('Um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta, confira o resultado abaixo: ')

    if operador == '+':
        soma = numero1_float + numero2_float
        print('Soma')
        print('{} + {} = {}'.format(numero1_float, numero2_float, soma))
    
    elif operador == '-':
        subtracao = numero1_float - numero2_float
        print('Subtração')
        print('{} - {} = {}'.format(numero1_float, numero2_float, subtracao))

    elif operador == '*':
        multiplicacao = numero1_float * numero2_float
        print('Multiplicação')
        print('{} * {} = {}'.format(numero1_float, numero2_float, multiplicacao))

    elif operador == '/':
        divisao = numero1_float / numero2_float
        print('Divisão')
        print('{} / {} = {}'.format(numero1_float, numero2_float, divisao))

    sair = input('Digite "S" ou "Sair" para sair da calculadora: ').lower()
    if sair == 's' or sair == 'sair':
        break
    else:
        continue

print('Você saiu da calculadora!')