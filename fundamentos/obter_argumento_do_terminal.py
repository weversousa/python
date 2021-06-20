from sys import argv

if __name__ == '__main__':
    print(argv)

# No terminal será executado assim:
# python obter_argumento_do_terminal.py oi este é um teste

# Resultado:
# ['.\\obter_argumento_do_terminal.py', 'oi', 'este', 'é', 'um', 'teste']
# -----------------------------------------------------------------------------

# O nome do arquivo também é retornado
# Como isso para sabermos se foi passado um argumento é só vericar se o tamanho
# do argv é maior que 1.

if __name__ == '__main__':
    print(argv) if len(argv) > 1 else print('Não foram passados argumentos.')

# No terminal será executado assim:
# python obter_argumento_do_terminal.py

# Resultado:
# Não foram passados argumentos.
