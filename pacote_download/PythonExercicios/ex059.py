n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número: '))
opcao = 0
soma = 0
while opcao != 5:
    print(' [ 1 ] soma\n [ 2 ] subtrair \n [ 3 ] multiplicar \n [ 4 ] novos números \n [ 5 ] sair do programa')
    opcao = int(input('Qual é sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        subtrair = n1 - n2
        print('{} - {} = {}'.format(n1, n2, subtrair))
    elif opcao == 3:
        multiplicar = n1 * n2
        print('{} x {} = {}'.format(n1, n2, multiplicar))
    elif opcao == 4:
        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalidade. Tente novamente.')
print('Obrigado volte sempre')

















