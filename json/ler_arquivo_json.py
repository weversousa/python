from json import load

with open('json/arquivo_criado.json', 'r', encoding='utf8') as f:
    dic = load(f)

print(dic)
