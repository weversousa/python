from json import load

with open('json/arquivo_criado.json', 'r', encoding='utf8') as f:
    dic = load(f)

print(dic)

# Resultado:
# {'arroz': 28.3, 'feijão': 9.7, 'café': 11.3}
