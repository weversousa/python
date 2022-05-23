# Dicionário

A estrutura de dados Dicionário (dict) é composta por qualquer sequência de `chave: valor` envolvidos entre `'{}` e separados por `,`.

Sobre a Dicionário:
* classe
* não indexada
* heterogênea
* mutável
* aceita repetição (valor)
* não aceita repetição (chave)

Criando um dicionário de forma Literal, onde os valores são definidos no momento de sua criação.

*Exemplo*:
~~~python
endereco = {'cep': '05110-030', 'numero': '1235'}

print(endereco)
print(type(endereco))
~~~

*Saída*:
~~~python
{'cep': '05110-030', 'numero': '1235'}
<class 'dict'>
~~~

Criando um dicionário vazio, onde os valores são inseridos após a sua criação de forma Dinâmica.

*Exemplo*:
~~~python
pessoa = {}

pessoa['nome'] = 'Paula'
pessoa['sexo'] = 'feminino'
pessoa['idade'] = 24

print(pessoa)
print(type(pessoa))
~~~

*Saída*:
~~~python
{'nome': 'Paula', 'sexo': 'feminino', 'idade': 24}
<class 'dict'>
~~~

## Classe dict

A classe `dict` é uma classe nativa e através dela é possível criar um dicionário. E por ser uma classe possui métodos para trabalhar com seus elementos.

Vimos mais acima como criar uma lista de forma literal usando `{}` que a forma mais usada, porém abaixo um exemplo de como criar um dicionário através da classe `dict`.

*Exemplo*:
~~~python
mercado = dict([('arroz', 22.40), ('feijão', 9.32), ('café', 13.50)])
print(mercado)
print(type(mercado))

mercado = dict(arroz=22.40, feijao=9.32)
print(mercado)
print(type(mercado))
~~~

*Saída*:
~~~python
{'arroz': 22.4, 'feijão': 9.32, 'café': 13.5}
<class 'dict'>

{'arroz': 22.4, 'feijao': 9.32}
<class 'dict'>
~~~

### Função update

O método `update` pertence à classe dict e serve para unir dois dicionários ou para inserir novos valor a um dicionário já existente.

*Exemplo*:
~~~python
estados = {'SP': 'Osasco', 'RJ': 'Ipanema'}
novos_estados = {'BA': 'Serrinha'}

estados.update(novos_estados)
print(estados)
~~~

*Saída*:
~~~python
{'SP': 'Osasco', 'RJ': 'Ipanema', 'BA': 'Serrinha'}
~~~

### Função key

O método `key` pertence à classe dict e retorna as chaves de um dicionário em forma de objeto `dict_keys` que é semelhante a lista visualmente, mas não é uma lista, porém para converter em uma lista é só passar esse objeto para a classe `list`.

*Exemplo*:
~~~python
endereco = {
    'logradouro': 'Avenida Paulista',
    'numero': '1235',
    'bairro': 'Consolação'
}

print(endereco.keys())
print(list(endereco.keys()))
~~~

*Saída*:
~~~python
dict_keys(['logradouro', 'numero', 'bairro'])
['logradouro', 'numero', 'bairro']
~~~

### Função values

O método `values` pertence à classe dict e retorna as chaves de um dicionário em forma de objeto `dict_values` que é semelhante a lista visualmente, mas não é uma lista, porém para converter em uma lista é só passar esse objeto para a classe `list`.

*Exemplo*:
~~~python
endereco = {
    'logradouro': 'Avenida Paulista',
    'numero': '1235',
    'bairro': 'Consolação'
}

print(endereco.values())
print(list(endereco.values()))
~~~

*Saída*:
~~~python
dict_values(['Avenida Paulista', '1235', 'Consolação'])
['Avenida Paulista', '1235', 'Consolação']
~~~

### Função items

O método `items` pertence à classe dict e retorna uma Lista de Tuplas, onde cada Tupla contém 2 itens separados por `,`, a chave e o valor de cada elemento de um dicionário, em forma de objeto `dict_items` que é semelhante a lista visualmente, mas não é uma lista, porém para converter em uma lista é só passar esse objeto para a classe `list`.

*Exemplo*:
~~~python
letras = {'a': 1, 'b': 2, 'c': 3}

print(letras.items())
print(list(letras.items()))
~~~

*Saída*:
~~~python
dict_itemes([('a', 1), ('b', 2), ('c', 3)])
[('a', 1), ('b', 2), ('c', 3)]
~~~

### Função get

O método `get` pertence à classe dict e retorna o valor de uma chave solicitada. Esse método recebe dois argumentos, o 1º é a chave procurada e o 2º é o que você deseja retornar caso a chave não exista, se não for passado o 2º argumento por padrão retorna `None`.


*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print(produtos.get('cafe', 'Chave não encontrada.'))
print(produtos.get('nescau', 'Chave não encontrada.'))
print(produtos.get('acucar'))
~~~

*Saída*:
~~~python
9.9
Chave não encontrada.
None
~~~

#### Notação colchetes

Também é possível acessar uma chave atráves de `[]`, mas se a chave não existir o programa gera um erro.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print(produtos['cafe'])
print(produtos['nescau'])
~~~

*Saída*:
~~~python
9.9
KeyError
~~~

Podemos deletar um elemento através da plavara reservada `del`, mas caso a chave não exista vai ser gerado um erro.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

del produtos['cafe']
print(produtos)

del produtos['açucar']
~~~

*Saída*:
~~~python
{'arroz': 28.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}

KeyError
~~~

#### Operador de associação

Podemos verificar se existe uma determinada chave no dicionário usando os operadores de **associação** `in` ou `not in`.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print('leite' in produtos)
print('banana' in produtos)

print('sal' not in produtos)
~~~

*Saída*:
~~~python
True
False

True
~~~

Também é possível verificar se determinado valor existe.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print(3.40 in produtos.values())
print(100.00 in produtos.values())
~~~

*Saída*:
~~~python
True
False
~~~

### Função pop

O método `pop` pertence à classe dict e remove uma elemento chave/valor do dicionário conforme a chave solicitada. Esse método recebe dois argumentos, o 1º é a chave procurada e o 2º é o que você deseja retornar caso a chave não exista, se não for passado o 2º argumento por padrão retorna `None`.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print(produtos.pop('tomate', 'Chave não encontrada.'))
print(produtos.pop('açucar', 'Chave não encontrada.'))
print(produtos.pop('sal'))

print(produtos)
~~~

*Saída*:
~~~python
2.89
Chave não encontrada.
None

{'arroz': 28.9, 'cafe': 9.9, 'shampoo': 12.99, 'leite': 3.4}
~~~

## Função len

O método `len` é nativo e retorna o tamanho do dicionário(quantidade de elementos) baseado nas chaves.

*Exemplo*:
~~~python
produtos = {
    'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4
}

print(len(produtos))
~~~

*Saída*:
~~~python
5
~~~

## Função sorted

O método `sorted` é nativo e podemos usá-lo para ordenar um dicionário por ordem crescente e decrescente.

Se passado somente o dicionário para o método `sorted`, ele vai pegar somente as chaves em forma de lista conforme quando é usado o método `keys` da classe `list`, e vai ordenar essas chaves, por padrão é ordenado em ordem crescente, para ordenar em ordem decrescente passar o parâmetros `reverse=True`, após isso será retornardo uma Lista.

*Exemplo*:
~~~python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

print(sorted(letras))
print(sorted(letras, reverse=True))
~~~

*Saída*:
~~~python
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
~~~

Para obter uma lista dos **valores** ordenados, nesse caso devemos especificar o método `values` que pertence a classe `dict`.

*Exemplo*:
~~~python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

print(sorted(letras.values()))
print(sorted(letras.values(), reverse=True))
~~~

*Saída*:
~~~python
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
~~~

Até agora o nosso retorno foi uma lista ou somente de chaves ou somente de valores.

Mas e se a gente quiser ordenar pela chave ou pelo valor e obter o nosso dicionário na forma original porém ordenado?

Para isso temos que usar o método `items` que pertence a classe `dict`.

Por padrão é ordenado em ordem crescente e pelas chaves, para ordenar em ordem decrescente passar o parâmetros `reverse=True`

O retorno dessa vez será uma Lista, e cada par de `chave: valor` do dicionário uma Tupla dessa lista.
E por fim, bastar usar a classe `dict` para transformar essa Lista em Dicionário.

*Exemplo*:
~~~python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

print(sorted(letras.items()))
print(sorted(letras.items(), reverse=True))

print(dict(sorted(letras.items())))
print(dict(sorted(letras.items(), reverse=True)))
~~~

*Saída*:
~~~python
[('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
[('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]

{'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
{'u': 5, 'o': 4, 'i': 3, 'e': 2, 'a': 1}
~~~

Para obter um retorno igual acima, porém ordenado pelo "valor" é necessário usar o parâmetro `key` do `sorted`, e o valor desse parâmetro é uma função.
Nessa função é feito a lógica por onde o método `sorted` deverá ordenar.
Já vimos que o método `items` que pertence a classe `dict` retorna uma Lista de Tuplas, sendo `(chave, valor)`, e já sabemos que a Tupla é indexada, logo é só definir na nossa função que o valor nesse caso **índice 1 da tupla** pois a chave é o índice 0, é quem será o fator de ordenação.

*Exemplo*:
~~~python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

print(sorted(letras.items(), key=lambda letras: letras[1]))
print(sorted(letras.items(), key=lambda letras: letras[1], reverse=True))
~~~

*Saída*:
~~~python
[('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
[('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]

{'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
{'u': 5, 'o': 4, 'i': 3, 'e': 2, 'a': 1}
~~~

Vamos criar um exemplo mais complexo, no dia a dia não vamos ter somente chaves e valor de 1 nível, vamos ter valores que são outro elemento chave/valor que por sua vez terá outro elemento chave/valor.

E se a gente quiser ordenar pelo valor de uma chave em um nível mais profundo?

Vamo usar um exemplo, onde eu quero ordenar o meu dicionário que terá o **nome cadastro** pelo valor que está dentro da **chave estado** que por sua vez está dentro da **chave endereco** onde está também está dentro de outra chave que é **dados_pessoais**.

*Exemplo*:
~~~python
cadastro = {
    1: {
        'dados_pessoais': {
            'nome': 'Weverton',
            'endereco': {
                'logradouro': 'Rua Armênia, 715',
                'estado': 'São Paulo'
            }
        }
    },
    2: {
        'dados_pessoais': {
            'nome': 'Maria',
            'endereco': {
                'logradouro': 'Rua Ford, 234',
                'estado': 'Bahia'
            }
        }
    },
    3: {
        'dados_pessoais': {
            'nome': 'Paula',
            'endereco': {
                'logradouro': 'Rua Sé, 100',
                'estado': 'Minas Gerais'
            }
        }
    }
}


def ordenar_por(cadastro_dict_items):
    return cadastro_dict_items[1]['dados_pessoais']['endereco']['estado']


cadastro_ordenado = dict(sorted(cadastro.items(), key=ordenar_por))
print(cadastro_ordenado)
~~~

*Saída*:
~~~python
{
    2: {
        'dados_pessoais': {
            'nome': 'Maria',
            'endereco': {
                'logradouro': 'Rua Ford, 234',
                'estado': 'Bahia'
            }
        }
    }, 
    3: {
        'dados_pessoais': {
            'nome': 'Paula',
            'endereco': {
                'logradouro': 'Rua Sé, 100', 
                'estado': 'Minas Gerais'
            }
        }
    },
    1: {
        'dados_pessoais': {
            'nome': 'Weverton',
            'endereco': {
                'logradouro': 'Rua Armênia, 715',
                'estado': 'São Paulo'
            }
        }
    }
}
~~~