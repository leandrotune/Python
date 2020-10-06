# Aprovando um empréstimo

print('bem vindo! \nA minha casa minha vida')
valor = float(input('Qual é o valor da casa: R$'))
salário = float(input('Qual é o valor do seu salário: R$'))
anos = int(input('Com quantos anos pretende pagar a casa 1 há 30 anos:'))
parcela = valor / (anos * 12)
porcentagem = salário * 30 / 100
if parcela <= porcentagem:
    print('Seu empréstimo foi aprovado')
    print('Você vai ter que pagar: R${:.2f} por mês'.format(parcela))
else:
    print('Infelismente seu emprestimo foi negado')