nomes_pesado = []
nomes_leve = []
pesado = []
leve = []
quantidade = 0

def linha():
    print('-' * 80)


linha()
while True:
    nome = str(input('nome: '))
    p = int(input('Peso: '))
    resp = str(input('quer continuar: ')).strip().upper()[0]
    quantidade += 1
    if resp == 'N':
        break
    if p > 70:
        pesado.append(p)
        nomes_pesado.append(nome)
    else:
        leve.append(p)
        nomes_leve.append(nome)
linha()
print(f'Ao todo, você cadastrou {quantidade} pessoas.')
print(f'O maior peso foi de {pesado}Kg. Peso de {nomes_pesado}')
print(f'O menor peso foi de {leve}Kg. Peso de {nomes_leve}')