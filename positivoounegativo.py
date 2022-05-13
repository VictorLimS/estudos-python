'''
Faça um programa que peça um valos e diga se é positivo ou negativo
'''


valor = int(input('Digite um número: '))

if (valor < 0):
    print(f'O número {valor} é negativo')
elif (valor > 0):
    print(f'O número {valor} é positivo')
else:
    print(f'O número digitado é nulo')
