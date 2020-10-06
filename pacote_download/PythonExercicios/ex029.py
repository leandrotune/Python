# Radar de multa:

carro = float(input('Em que velocidade seu carro estava rodado ? '))
multa = (carro - 80) * 7
if carro <= 80:
    print('Bom dia! Dirija com segurança!')
else:
    print('MULTADO! você excedeu o mimite de 80km/h')
    print('Você deve pagar uma multa de: R${}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
