from json import load

caminho_arquivo = 'manipulacao_de-arquivos/extensao-json/arquivo_criado.json'
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    dicionario = load(arquivo)

print(dicionario)

# Resultado:
# {'arroz': 28.3, 'feijão': 9.7, 'café': 11.3}
