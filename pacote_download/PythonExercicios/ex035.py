#podem formar um triângulo

print('\033[1:31m='*50)
print('\033[1:30mAnalizador de Triângulos')
print('\033[1:31m='*50)
r1 = float(input('\033[1:34mPrimerio segmento: '))
r2 = float(input('\033[1:34mSegundo segmento: '))
r3 = float(input('\033[1:34mTerceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1:33mOs segmentos podem formar um Triângulo: ')
else:
    print('\033[1:33mOs segmentos não podem formar um Triângulo')

