from csv import reader, writer, DictReader, DictWriter

# Lendo arquivo
caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-csv/telefones.csv'

with open(file=caminho_do_arquivo, mode='r') as arquivo:
    telefones = reader(arquivo)

    for linha in telefones:
        print(linha)

# Resultado:
# ['ddd', 'telefone', 'nome']
# ['11', '999999999', ' Maria']
# ['75', '988888888', ' Pedro']
# -----------------------------------------------------------------------------

# Criando e escrvendo arquivo
caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-csv/brasileirao.csv'

with open(caminho_do_arquivo, 'w', newline='') as arquivo:
    brasileirao = writer(arquivo)

    brasileirao.writerow(['Posição', 'Time', 'Pontos'])
    brasileirao.writerow(['1', 'São Paulo', '25'])
    brasileirao.writerow(['2', 'Vasco', '22'])
    brasileirao.writerow(['3', 'Bahia', '18'])

# Resultado:
# Será criado um arquivo CSV no caminho e com o nome que vou estabeleceu.
# -----------------------------------------------------------------------------

# Gravando arquivo com delimitador de tabulação
with open(caminho_do_arquivo, 'w') as arquivo:
    brasileirao = writer(arquivo, delimiter='\t')

    brasileirao.writerow(['Posição', 'Time', 'Pontos'])
    brasileirao.writerow(['1', 'São Paulo', '25'])
    brasileirao.writerow(['2', 'Vasco', '22'])
    brasileirao.writerow(['3', 'Bahia', '18'])

# Resultado:
# Será criado um arquivo CSV no caminho e com o nome que vou estabeleceu.
# -----------------------------------------------------------------------------

# Gravando várias linhas de uma vez
dados = [
    ['Código', 'Sigla', 'Estado'],
    [1, 'BA', 'Bahia'],
    [2, 'SP', 'São Paulo']
]

caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-csv/estados.csv'

with open(caminho_do_arquivo, 'w', newline='') as arquivo:
    estados = writer(arquivo)
    estados.writerows(dados)

# Resultado:
# Será criado um arquivo CSV no caminho e com o nome que vou estabeleceu.
# -----------------------------------------------------------------------------

# Com Python podemos ler um CSV como um dicionário, usando a classe DictReader
with open(caminho_do_arquivo, 'r', newline='') as arquivo:
    estados = DictReader(arquivo)

    print(estados)

    for linha in estados:
        print(linha)


# Resultado:
# <csv.DictReader object at 0x0000028143842790>
# {'Código': '1', 'Sigla': 'BA', 'Estado': 'Bahia'}
# {'Código': '2', 'Sigla': 'SP', 'Estado': 'São Paulo'}
# -----------------------------------------------------------------------------

# Transformar um Dicionário em um CSV

itens = [
    {'nome': 'computador', 'preco': 2300.99},
    {'nome': 'televisao', 'preco': 1870.99}
]


caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-csv/produtos.csv'

with open(caminho_do_arquivo, 'w', newline='') as arquivo:

    # O nome dos cabeçalhos é igual aos nomes das chaves do Dicionário
    cabecalho = ['nome', 'preco']
    produtos = DictWriter(arquivo, fieldnames=cabecalho)

    produtos.writerows(itens)

# Resultado:
# Será criado um arquivo CSV no caminho e com o nome que vou estabeleceu.
# -----------------------------------------------------------------------------

# Usando a biblioteca Pandas

from pandas import DataFrame

# Criamos um Data Frame (Quadro de Dados)
df = DataFrame(
    [
        ['Neymar', 'Brasil'],
        ['C. Ronaldo', 'Portugal'],
        ['Messi', 'Argentina']
    ],
    columns=['Jogador', 'País'],
)

# Transferimos o Data Frame para o CSV
caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-csv/jogadores.csv'
df.to_csv(caminho_do_arquivo, encoding='utf8', index=None)
