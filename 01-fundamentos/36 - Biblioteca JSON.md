# JSON

Podemos criar um arquivo `JSON` de forma literal.
É necessário envolver toda a informação entre aspas simples, pois cada chave em um arquivo `JSON` é escrito com aspas duplas e cada valor textual também.

*Exemplo*:
~~~python
dados = '''[{
    "nome": "Weverton",
    "salário": 3500,
    "linguagens": ["Python", "Java"],
    "empregado": true
}]'''

with open('.json', 'w', encoding='utf-8') as arquivo:
    arquivo.write(dados)
~~~

*Saída*:

Vai ser criado um arquivo `.json` em seu pc.

## Biblioteca json

### Atributos dumps e dump

O atributo `dumps` é uma função que recebe um objeto no padrão de um arquivo JSON e retorna uma String com formato válido de um JSON, corrigindo algumas sintaxes que seriam válidas somente no Python para a sintaxe Javascript.

Por exemplo, abaixo os números com `_` que no Python podemos usar para separar milhar o valor `True` que no Python a letra **T** é em maiúsculo vão ser adaptados para o padrão JS que não aceita nenhum dos dois formatos.

Podemos usar a função `write` dos arquivos abertos com `open`.

O atributo `dump` é uma função que faz exatamente as mesmas coisas que o atributo acima, porém não retorna nada, essa função salva os dados em um arquivo externo. Nesse caso não é necessário usar a função `write`, pois a própria função `dump` faz isso.

*Exemplo*:
~~~python
from json import dumps, dump


funcionarios = [{
    'nome': 'Weverton',
    'salário': 3_500,
    'linguagens': ['Python', 'Java'],
    'empregado': True
}]

with open('.json', 'w', encoding='utf-8') as arquivo:
    arquivo.write(dumps(funcionarios, ensure_ascii=False, indent=4))

with open('.json', 'w', encoding='utf-8') as arquivo:
    dump(funcionarios, arquivo, ensure_ascii=False, indent=4, sort_keys=True)
~~~

### Atributos loads e load


Os atributos `loads` e `load` são funções da biblioteca `JSON`.
Ambos convertem um JSON válido para uma estrutura Python.

A diferença é que a função `loads` recebe um valor literal (um texto).

*Exemplo*:
~~~python
from json import loads, load


funcionarios = loads('''[{
    "nome": "Weverton",
    "salário": 3500,
    "linguagens": ["Python", "Java"],
    "empregado": true
}]''')

print(type(funcionarios))
print(funcionarios)

pessoa = loads('{"nome": "Weverton", "cidade": "Osasco"}')

print(type(pessoa))
print(pessoa)
~~~

*Saída*:
~~~python
<class 'list'>
[{'nome': 'Weverton', 'salário': 3500, 'linguagens': ['Python', 'Java'], 'empregado': True}]

<class 'dict'>
{'nome': 'Weverton', 'cidade': 'Osasco'}
~~~

Ja a função `load` recebe um objeto, exemplo: quando abrimos um arquivo `JSON` com a função `open` o retorno dessa função é um objeto.

*Exemplo*:
~~~python
from json import load
from os.path import exists


if exists('.json'):
    with open('.json', 'r', encoding='UTF-8') as arquivo:

        print(type(arquivo))
        print(arquivo)

        funcionario = load(arquivo)
        print(type(funcionario))
        print(funcionario)
~~~

*Saída*:
~~~python
<class '_io.TextIOWrapper'>
<_io.TextIOWrapper name='.json' mode='r' encoding='UTF-8'>

<class 'list'>
[{'empregado': True, 'linguagens': ['Python', 'Java'], 'nome': 'Weverton', 'salário': 3500}]
~~~