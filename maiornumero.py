'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O {num1} é maior que o {num2}')
elif num1 < num2:
    print(f'o {num2} é maior que o {num1}')
else:
    print('Os dois números são iguais')