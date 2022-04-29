from datetime import datetime

trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho ( 0 não tem)'))
if trabalhador['ctps'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contatação: '))
    trabalhador['Salario'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'-{k} tem o valor {v}')

