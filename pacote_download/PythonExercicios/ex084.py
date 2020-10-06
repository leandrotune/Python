dados = []
cadastrados = 0
pesado = []
leve = []
nomes_leves = []
nomes_pesados = []

def linha():
    print('-' * 80)

linha()
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(int(input('Peso: ')))
    cadastrados += 1
    resp = str(input('Quer continuar: ')).upper()[0]
    if resp == 'N':
        break
    if dados[1] <= 70:
        leve.append(dados[1])
        nomes_leves.append(dados[0])
    if dados[1] > 70:
        pesado.append(dados[1])
        nomes_pesados.append(dados[0])
linha()
print(f'Ao todo, você cadastrou {cadastrados}')
print(f'O maior peso foi {pesado}Kg. Peso de {nomes_pesados}')
print(f'O menor peso foi {leve}Kg. Peso de {nomes_leves}')
linha()







