# Calculo feito para descobrir o valor da hipotenusa: (ca**2 + co**2) **(1/2) #

ca = float(input('Comprimento do cateto oposto:'))
co = float(input('comprimeiro do cateto asjacente:'))
hi = (ca**2 + co**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#função da hipotenusa: hipot

from math import hypot
ca = float(input('comprimento do cateto oposto: '))
co = float(input('coomprimento do cateto adjacente: '))
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))





