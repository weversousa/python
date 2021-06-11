fruta1 = {}

# Atribuindo Chave / Valor
fruta1['nome'] = 'uva'
fruta1['preco'] = 3.99

# Atribuindo de forma Literal
fruta2 = {
    'nome': 'abacai',
    'preco': 4.55
}

# Alterando o valor de uma Chave
fruta2['nome'] = 'melão'

# Dicionário dentro de um dicionário
endereco = {
    'cidade': 'Osasco',
    'bairro': 'Altino',
    'cep': {
        '06210050': {
            'tipo_logradouro': 'Rua',
            'logradouro': 'Ana Zozi Toni',
            'numero': 1000
        }
    }
}


# Acessando
endereco['cep']['06210050']['logradouro']  # Ana Zozi Toni

# Percorrendo um Dicionário
pessoa = {'nome': 'Paula', 'idade': 30, 'sexo': 'feminino'}

for chave, valor in pessoa.items():
    print(chave, valor)

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave in pessoa:
    print(pessoa[chave])


frutas = [('maçã', 2.30), ('bana', 5.40)]
frutas = dict(frutas)
print(frutas)
