valores = []
resp = ' '
encontrado = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar: ')).strip().upper()
    if resp == 'N':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}')
if 5 in valores:                                          # se o 5 estiver em valores
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')








