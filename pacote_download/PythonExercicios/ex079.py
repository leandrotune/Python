valores = []

while True:
    n = int(input('Digite um número: '))
    if n not in valores:                        # se n naõ estive in valores adicionar.
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
print(f'=-' * 30)
print(f'Você digitou os valores: {sorted(valores)}')