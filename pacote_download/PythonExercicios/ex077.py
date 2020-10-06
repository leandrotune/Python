def linha():
    print('=' * 50)
linha()
print(f'{"VOGAIS das palavras":^50}')
linha()
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
          'MERCADO', 'PROGRAMADOR', 'FUTURO')
for vogal in palavras:
        print(f'\nNA palavra {vogal} temos', end=' ')
        for letra in vogal:
            if letra in 'AEIOU':
                print(letra, end=' ')

