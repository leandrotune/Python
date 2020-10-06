# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:                                                      # enquanto n for verdairo ele vai continuar.
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:                                                    # se n for negativo o programa vai finalizar
        break
    print('-' * 45)
    for c in range(1, 11):                                       # vai fazer 1 até 10 
        print(f'{n} x {c} = {n * c}')
    print('-' * 45)
print('tabuada encerrada, volte sempre')

# nesse programa não precisei usar um contador.



