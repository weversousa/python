from json import dump

dic = {}

dic['arroz'] = 28.30
dic['feijão'] = 9.70
dic['café'] = 11.30

caminho_arquivo = 'manipulacao_de-arquivos/extensao-json/arquivo_criado.json'

with open(caminho_arquivo, 'w', encoding='utf8') as f:
    dump(dic, f, ensure_ascii=False)

print('Arquivo JSON criado com sucesso.')
