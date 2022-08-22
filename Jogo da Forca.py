import getpass
import os

secreto = getpass.getpass('Digite uma palavra secreta: ')
digitadas = []
chances = 10

while True:
    letra = input('Jogador 2: Digite uma letra: ')

    if len(letra) > 1:
        print('Não vale! Você deve digitar apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Você acertou uma letra!')
    else:
        print('Que pena! essa letra não existe na palavra secreta.')
        chances -= 1
        print(f'Você ainda tem {chances} chances')
        if chances == 0:
            print('Você perdeu, suas chances acabaram.')
            break

        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns, você acertou! A palavra secreta era {secreto}')
        os.system('restart')

    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')






