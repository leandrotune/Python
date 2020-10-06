# média da nota

portugues = float(input('\033[1:31mNota de Português: '))
matematica = float(input('\033[1:31mNota de Matemática: '))
media = (portugues + matematica) / 2
if media < 5.0:
    print('\033[1:30mREPROVADO')
elif media == 5.0 and media <= 6.9:
    print('\033[1:32mRECUPERAÇÃO')
elif media > 7.0:
    print('\033[1:34mAPROVADO')
