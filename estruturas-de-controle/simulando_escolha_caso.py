# Python não possui a estrutura Swich, mas podemos simular sua funcionalidade.

def escolha_dia_da_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    return dias.get(dia, 'Esse dia não existe!!')


if __name__ == '__main__':
    print(escolha_dia_da_semana(3))
    print(escolha_dia_da_semana(11))

# Resultado:
# Terça
# Esse dia não existe!!
