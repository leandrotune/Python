print('\033[1:30m''='*50)
print('\033[1:32mAnalizando se o Triângulo é:')
print('\033[1:30m''='*50)
print('\033[1:31mEquilátero:\033[m\033[1:30mtodos os lados iguais\033[m')
print('\033[1:31mIsósceles:\033[m\033[1:30mdois lados iguais')
print('\033[1:31mEscaleno:\033[m\033[1:30mtodos os lados diferentes\033[m')
print('\033[1:30m''='*50)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 > r2 + r3 and r2 > r1 + r3 and r3 > r1 + r2:
    print('Os segmentos não forma um Triângulo')

elif r1 == r2 and r1 == r3 and r2 == r1 and r2 == r3 and r3 == r1 and r3 == r2:
    print('O triângulo é Equilátero')

elif r1 == r2 and r2 == r3 and r3 == r1:
    print('O Triangulo é Isósceles')

elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r1 and r3 != r2:
    print('O triângulo é Escaleno')







