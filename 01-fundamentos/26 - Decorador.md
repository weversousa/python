# Decorador

Um decorador é uma função que vai receber como argumento outra função. E assism é possível executar realizar outra tarefa antes ou depois da função principal ser executada.

Para usar uma função como decorador é só inserir essa função com um `@` no começo, logo na linha acima da função que será enviada a ela.

Dentro da função decoradora vai ter outra função que é quem vai executar as tarefas e também executar a função original, caso a função original tenha parâmetros os mesmos devem ser informados também nessa função interna.

*Exemplo*:
~~~python
def funcao_decorador(minha_funcao):

    def wrapper(nome):
        print('===== Cabeçalho =====')
        minha_funcao(nome)
        print('===== Rodapé =====')

    return wrapper


@funcao_decorador
def exibr_nome(nome):
    print(f'Olá senhor (a) {nome}.')


exibr_nome('Jaqueline')

~~~

*Saída*:
~~~python
===== Cabeçalho =====
Olá senhor (a) Jaqueline.
===== Rodapé =====
~~~