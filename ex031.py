distancia = float(input('Qual a distancia de dua viagem ? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem será de R${:.2f}'.format(preco))
