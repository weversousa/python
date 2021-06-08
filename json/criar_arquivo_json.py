from json import dump

dic = {}

dic['arroz'] = 28.30
dic['feijão'] = 9.70
dic['café'] = 11.30

with open('json/arquivo_criado.json', 'w', encoding='utf8') as f:
    dump(dic, f, ensure_ascii=False)

print('Arquivo JSON criado com sucesso.')
