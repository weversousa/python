from pandas import DataFrame

df = DataFrame({
    'produto': ['arroz', 'feijão', 'manteiga', 'café'],
    'preco': [19.90, 7.80, 4.30, 11.90],
    'qtde': [2, 4, 3, 2]
})


# SQL:
# SELECT produto, preco, qtde FROM df LIMIT 2;
print(df[['produto', 'preco', 'qtde']])

#     produto  preco  qtde
# 0     arroz   19.9     2
# 1    feijão    7.8     4
# -----------------------------------------------------------------------------

# SQL:
# SELECT *, preco * qtde AS "total" FROM df;
print(df.assign(total=df['preco'] * df['qtde']))

#     produto  preco  qtde  total
# 0     arroz   19.9     2   39.8
# 1    feijão    7.8     4   31.2
# 2  manteiga    4.3     3   12.9
# 3      café   11.9     2   23.8
# -----------------------------------------------------------------------------

# SQL:
# SELECT * FROM df WHERE produto = 'café';
print(df[df['produto'] == 'café'])

#   produto  preco  qtde
# 3    café   11.9     2
# -----------------------------------------------------------------------------

# SQL:
# SELECT * FROM df WHERE prodtudo = 'arroz' AND preco > 18.0;
print(df[(df['produto'] == 'arroz') & (df['preco'] > 18.0)])

#   produto  preco  qtde
# 0   arroz   19.9     2
# -----------------------------------------------------------------------------

# SQL:
# SELECT * FROM df WHERE prodtudo OR 'manteiga' AND preco > 19.0;
print(df[(df['produto'] == 'manteiga') | (df['preco'] > 19.0)])

#     produto  preco  qtde
# 0     arroz   19.9     2
# 2  manteiga    4.3     3
# -----------------------------------------------------------------------------

