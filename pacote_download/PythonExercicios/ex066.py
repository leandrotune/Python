'''num = cont = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num != 999:
        cont += 1                                                   # primeira forma de fazer
        soma += num
    else:
        break
print(f'A soma dos {cont} valores foi {soma}!'''


soma = cont = 0
while True:
    num = (int(input('Digite um número (999 para parar): ')))
    if num == 999:
        break                                                       # segundo forma de fazer a mais correta
    cont += 1                                                       # mais adicionar um contador depois do break
    soma += num                                                     # e só colocar fora do break
print(f'A soma dos {cont} valores foi {soma}!')

