nome = input('Digite seu nome completo: ').strip()
print('Seu nome completo com todas as letras maiusculas: \n{}'.format(nome.upper()))
print('Seu nome com todas as letras minusculas: \n{}'.format(format(nome.lower())))
print('Seu nome tem:\n{} caracteres sem os espaços.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é:\n{} e tem {} caracteres'.format(dividido[0], len(dividido[1])))






