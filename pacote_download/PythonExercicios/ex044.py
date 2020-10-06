print('\033[1:32mSUPERMERCADO')

preço = float(input('Preço do produto: '))
pagamento = input('Forma de pagamento: ').lower()

dinheiro = preço - (preço * 10) / 100  # Desconto 10%
cartao = preço - (preço * 5) / 100  # Desconto 5%
cartao2 = preço     # Preço normal
parcelado = preço + (preço * 20) / 100   # Furos de 20%

if pagamento == 'dinheiro':     # pagamento no dinheiro
    print('O total á pagar é R${}'.format(dinheiro))

elif pagamento == 'cartão pagamento a vista' or pagamento =='pagamento no cartão a vista':   # Pagamento no cartão a vista
    print('O total á pagar é R${}'.format(cartao))

elif pagamento == 'cartão 2 vezes' or pagamento == 'parcelado 2 vezes': # Pagamento no cartão 2 vezes
    print('O valor total á pagar é R${}'.format(cartao2))

elif pagamento == 'cartão 3 vezes':                  # Pagamento no cartão 3 vezes
    print('O valor total é {}'.format(parcelado))





