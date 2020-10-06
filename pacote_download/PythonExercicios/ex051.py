# Desenvolva um programa que leia:
# o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(30*'=')
print('     10  TERMOS DE UMA PA')
print(30*'=')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão     # calculo para saber o decimo termo da PA
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' ')
print('Acabou')
