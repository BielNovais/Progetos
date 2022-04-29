def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='')
            cont += p
        print('FIM !')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ')
            cont -= p
        print('FIM')


contador (1, 10, 1)