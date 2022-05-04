import CNPJ

cnpj1 = '04.252.011/0001-10'

if CNPJ.valida(cnpj1):
    print(f'{cnpj1} é valido')
else:
    print(f'{cnpj1} é invalido')
