'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input('Digite a letra F para Feminíno e M para Masculino ')

if letra.upper() == 'M':
    print(f'{letra} - Masculino')
elif letra.upper() == 'F':
    print(f'{letra} - Feminino')
else:
    print('Sexo inválido.')
