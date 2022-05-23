# Princípio de Design SOLID

* Código limpo
* Cada método é responsável por uma única ação

*Exemplo*:
~~~python
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__inidcar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        ...

    def __inidcar_erro(self):
        ...
~~~

## Princípio Fechado

Fechado, pois já estão definidas as opções.

*Exemplo*:
~~~python
class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        elif tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show.')

    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show.')
~~~

## Princípio Aberto

Aberto, pois são infinitas as opções a serem apresentadas.

A fragilidade dessa abordagem de associação é que toda classe passada para o objeto circo, obrigatoriamente deve ter o método apresentar_show.

*Exemplo*:
~~~python
class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando seu show.')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando seu show.')


circo = Circo()
palhaco = Palhaco()
malabarista = Malabarista()

circo.apresentar(palhaco)
circo.apresentar(malabarista)
~~~

*Saída*:
~~~python
Palhaço apresentando seu show.
Malabarista apresentando seu show.
~~~

### Uso real do Princípio Aberto/Fechado

Estrutura de pastas e arquivos para o projeto.

~~~poweshell
projeto
      L databases
                L postgre.py
                L sqlserver.py
      L main.py
      L repositorio.py
~~~


*Exemplo*:
~~~python
# databases/postgre.py

class PostgreSQL:
    def __init__(self) -> None:
        self.__conexao = 'PostgreSQL'

    def conectar(self) -> str:
        print('Conectando ao PostgreSQL')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do PostgreSQL')
~~~


*Exemplo*:
~~~python
# databases/sqlserver.py

class SQLServer:
    def __init__(self) -> None:
        self.__conexao = 'SQLServer'

    def conectar(self) -> str:
        print('Conectando ao SQLServer')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do SQLServer')
~~~


*Exemplo*:
~~~python
# databases/__init__.py

# Vai fazer com que as classes fiquem visíveis fora do pacote databases
from .postgres import PostgreSQL
from .sqlserver import SQLServer
~~~


*Exemplo*:
~~~python
# repositorio.py

class Repositorio:
    def select(self, db_connection: any) -> None:
        conn = db_connection.conectar()
        # Realizar ações...
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conn = db_connection.conectar()
        # Realizar ações...
        db_connection.desconectar()
~~~


*Exemplo*:
~~~python
# main.py

# Vai fazer com que as classes fiquem visíveis fora do pacote databases
from repositorio import Repositorio
from databases import PostgreSQL
from databases import SQLServer


# A classe Repositorio vai realizar suas ações independente do banco de dados

db_postgre = PostgreSQL()
repo = Repositorio()
repo.insert(db_postgre)
repo.select(db_postgre)

db_sqlserver = SQLServer()
repo = Repositorio()
repo.insert(db_sqlserver)
repo.select(db_sqlserver)
~~~