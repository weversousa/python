# Composição de Classes

A instância de uma classe dentro de outra é composição, uma forma de fugir da herança.

*Exemplo*:
~~~python
class Select:

    def select_one(self):
        print('SELECT * FROM database_name;')

    def select_many(self):
        print("SELECT * FROM database_name WHERE column_name = 'blá blá blá';")


class Repositorio:

    def __init__(self):
        self.__select = Select()

    def select_all(self):
        return self.__select.select_many()
~~~