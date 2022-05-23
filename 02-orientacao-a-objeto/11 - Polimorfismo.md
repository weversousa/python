# Polimorfismo

## Estático

É quando ocorre a sobrecarga de um método (o memso método ocorre mais de uma vez no código).

## Dinâmico

É quando você sobrescreve o método com um comportamento diferente na classe filha.

*Exemplo*:
~~~python
class Pizza:

    def ingredientes(self):
        return 'Ingredientes'


class Mussarela(Pizza):

    # Polimorfirmos
    def ingredientes(self):
        return ['queijo', 'tomate', 'orégano']
~~~