velocidade = float(input('Qual a velocidade atual do carro ?'))
if velocidade > 80:
    print('Você está acima do limite')
    multa = (velocidade - 80) * 7
    print('Você pagará um multa de {}'.format(multa))
print('Tenha um otimo dia !')


