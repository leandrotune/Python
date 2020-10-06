# indice de massa coporal

print('Calculadora de IMC')
peso = float(input('Peso ?'))
altura = float(input('Altura ?'))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Abaixo do peso')
    print('procure se alimentar mais!')
elif IMC >= 18.5 and IMC <= 24.9:
    print('Peso normal')
    print('Parabéns')
elif IMC >= 25 and IMC <= 34.9:
    print('Sobrepeso')
    print('procure fazer exercicio')
elif IMC >= 30 and IMC <= 34.9:
    print('Obesidade grau 1')
    print('procure se alimentar melhor e fazer mais exercicio')
elif IMC >= 35 and IMC <= 39.9:
    print('Obesidade grau 2')
    print('procure comer menos e fazer mais exercico e talvez seja hora de procurar ajudar')
elif IMC >= 40:
    print('Obesidade grau 3')
    print('você está em obesidade mobida procure ajudar')