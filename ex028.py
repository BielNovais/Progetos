from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ?'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens ! Você venceu !')
else:
    print('Ganhei ! pensei em numero {} e não no {}'.format(computador, jogador))
    
