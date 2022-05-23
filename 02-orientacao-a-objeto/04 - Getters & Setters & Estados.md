# Getters & Setters & Estados

* Nome da classe devem ser substantivo
* Nome dos métodos devem ser verbos

*Exemplo*:
~~~python
class Alarme:
    def __init__(self) -> None:
        self.__estado = False

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        # Método que verifica se um valor pertence a uma classe epecífica
        if isinstance(valor, bool):
            self.__estado = valor


alarme_1 = Alarme()
print(alarme_1.get_estado())

alarme_1.set_estado(True)
print(alarme_1.get_estado())
~~~

*Saída*:
~~~python
False
True
~~~