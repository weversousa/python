def cabecalho(f):

    def wrapper(nome):
        print('===== Cabeçalho =====')
        f(nome)
        print('===== Rodapé =====')

    return wrapper


@cabecalho
def exibr_nome(nome):
    print(f'Olá senhor {nome}.')


exibr_nome('Jaqueline')
