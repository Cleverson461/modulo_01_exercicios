from random import randint
from time import sleep

print(30 * '-=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print(30 * '-=')
print()
number = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
numero_aleatorio = randint(0, 5)

if number == numero_aleatorio:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero_aleatorio} e não no {number}!')
