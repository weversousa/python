import pandas as pd
import numpy as np

url = (
    'https://opendatasus.saude.gov.br/pt_BR/dataset'
    '/a2cfca72-d8e8-4878-b7f5-d97535a991d5/resource'
    '/77d8d14a-cf8c-4209-bed3-3b63ed63fd4f/download/arquivo_geral.csv'
)

info_covid_df = pd.read_csv(url, delimiter=';')

# SELECT *
# FROM info_covid_df LIMIT 5
print(info_covid_df.head(n=5))
# -----------------------------------------------------------------------------

# SELECT *, casosNovos - obitosNovos AS "sobreviveram"
# FROM info_covid_df
# WHERE casosNovos > 0
# LIMIT 5;
print(
    info_covid_df.assign(
        sobreviveram=info_covid_df['casosNovos'] - info_covid_df['obitosNovos']
    )[info_covid_df['casosNovos'] > 0].head(n=5)
)


# A instrução acima está simplesmente passando um Seriesobjeto True / False
# para o DataFrame, retornando todas as linhas com True.
casos_novos_maior_que_zero = info_covid_df['casosNovos'] > 0
print(casos_novos_maior_que_zero.value_counts())

# Resultado:
# False    1357
# True      992


# O mesmo exemplo da linha 20
print(
    info_covid_df.assign(
        sobreviveram=info_covid_df['casosNovos'] - info_covid_df['obitosNovos']
    )[casos_novos_maior_que_zero].head(n=5)
)
# -----------------------------------------------------------------------------

# SELECT regiao, casosNovos
# FROM info_covid_df
# WHERE regiao = 'Sudeste' AND casosNovos > 900
print(
    info_covid_df.loc[
        (info_covid_df['regiao'] == 'Sudeste') & (info_covid_df['casosNovos'] > 900),
        ['regiao', 'casosNovos']
    ]
)
# -----------------------------------------------------------------------------

# SELECT regiao, casosNovos
# FROM info_covid_df
# WHERE casosNovos < 100 OR obitosNovos > 100

print(
    info_covid_df.loc[
        (info_covid_df['casosNovos'] < 100) | (info_covid_df['casosNovos'] > 100),
        ['regiao', 'casosNovos', 'obitosNovos']
    ]
)
# -----------------------------------------------------------------------------

# SELECT *
# FROM info_covid_df
# WHERE casosNovos IS NULL;
info_covid_df[info_covid_df['casosNovos'].isna()]
# -----------------------------------------------------------------------------

# SELECT *
# FROM info_covid_df
# WHERE casosNovos IS NOT NULL;
info_covid_df[info_covid_df['casosNovos'].notna()]
# -----------------------------------------------------------------------------

# SELECT regiao, count(*)
# FROM tips
# GROUP BY regiao;
print(
    info_covid_df.groupby('regiao').size().reset_index(name='total')
)

print(
    info_covid_df.groupby('regiao')['regiao'].count().reset_index(name='total')
)
# -----------------------------------------------------------------------------

# SELECT estado, AVG(casosNovos), COUNT(*)
# FROM info_covid_df
# GROUP BY estado;
print(
    info_covid_df.groupby('estado').agg(
        {'casosNovos': np.mean, 'estado': np.size}
    )
)
# -----------------------------------------------------------------------------

df = pd.DataFrame({'numeros': [1, 2, 3, 3, 1, 4, 2]})
print(df['numeros'].unique())
