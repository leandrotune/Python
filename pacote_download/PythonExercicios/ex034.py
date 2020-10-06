salário = float(input('\033[1:30mSalário do funcionario? R$')) # mudar a cor da letra: \033[1:31m
if salário <=1500:
    novo = salário + (salário * 15 / 100)      # posso criar uma variavel dentro do if:
    print('\033[1:31mQuem ganhava {:.3f} passará a ganhar {:.3f}'.format(salário, novo))
else:
    novo = salário + (salário * 10 / 100)      # posso criar uma variavel dentro do else:
    print('\033[1:31mquem ganhava {:.3f} parrará a ganhar {:.3f}'.format(salário, novo))






