n1 = int(input('digite um número:'))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1**(1/2)
print('o número que você digitou é {} \n O seu dobro é {} \n O seu triplo é {} \n E sua raiz quadrada é {:.2f}'.format(n1, n2, n3, n4))
t1 = int(input('digite outro número:'))
print('você digitou {} \nO seu dobro é {} \nO seu triplo é {} \nE sua raiz quadrada é {:.2f}'.format(t1, (t1*2), (t1*3), t1**(1/2)))

# se nao precisa do resultado la na frente nao é preciso guardar o resultado em uma variavel.#
# basta colocar a soma dentro do comando format(  )#
# assim você poupará espaço na memoria. #