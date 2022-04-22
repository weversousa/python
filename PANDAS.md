`pip install pandas`

## Series
A Series representa "uma" coluna ou "uma" linha de um DataFrame.

### Criar `Series` de forma literal
~~~python
from pandas import Series


cidades = Series(data=['Osasco', 'Salvador', 'Recife'])
~~~
 
~~~python
print(type(cidades))



<class 'pandas.core.series.Series'>
~~~

~~~python
print(cidades)



0    Osasco    
1    Salvador    
2    Recife    
dtype: object
~~~

### Pegar os valores
~~~python
print(cidades.values)



['Osasco', 'Salvador', 'Recife']
~~~

### Pegar os índices
~~~python
print(cidades.index)



RangeIndex(start=0, stop=3, step=1)
~~~

### Nomear os índices na criação
~~~python
cidades = Series(
    data=['Osasco', 'Salvador', 'Recife'],
    index=['sp', 'ba', 'pe']
)
~~~

~~~python
print(cidades)



sp    Osasco
ba    Salvador
pe    Recife
dtype: object
~~~


~~~python
print(cidades.index)



Index(['sp', 'ba', 'pe'], dtype='object')
~~~

### Acessar os dados a partir do índice
Mesmo com índices nomeados é possível acessar pelo índice numérico.
~~~python
print(cidades['sp'])
print(cidades[0])



Osasco

Osasco
~~~

### Acessar os dados com **slice** a partir do índice
Lembrando que no slice o último valor não entra, 1:3 vai, do 1 ao 2.  
No slice pelo índice nomeado o último valor entra, 'BA':'RJ', vai do BA ao RJ.
~~~python
print(cidades[1:3])
print(cidades['BA':'RJ'])



BA    Salvador
RJ    Botafogo
dtype: object

BA    Salvador
RJ    Botafogo
dtype: object
~~~

### Métodos prontos
~~~python
numeros = Series([33, 33, 10, 21, 72, 4, 4])
~~~

~~~python
print(numeros)



0    33
1    33
2    10
3    21
4    72
5     4
6     4
~~~

#### Menor valor
~~~python
print(numeros.min())



4
~~~

#### Maior valor
~~~python
print(numeros.max())



72
~~~

#### Soma dos valores
~~~python
print(numeros.sum())



177
~~~

#### Média
~~~python
print(numeros.mean())



25.285714285714285
~~~

#### Mediana
~~~python
print(numeros.median())



21.0
~~~

#### Valores únicos
~~~python
print(numeros.unique())



[33 10 21 72  4]
~~~

#### Agrupar e contar os valores
~~~python
print(numeros.value_counts())



33    2
4     2
10    1
21    1
72    1
dtype: int64
~~~

#### Resumo dos campos numéricos
~~~python
print(numeros.describe())



count     5.000000
mean     28.000000
std      26.972208
min       4.000000
25%      10.000000
50%      21.000000
75%      33.000000
max      72.000000
dtype: float64
~~~

### Máscaras (Filtros)
~~~python
print(frutas >= 5.00)
print(frutas[frutas >= 5.00])



Uva       True
Limão    False
Manga     True
dtype: bool

Uva      5.9
Manga    5.1
dtype: float64
~~~

~~~python
print(frutas[frutas >= 5.00].index)
print(frutas[frutas >= 5.00].values)



Index(['Uva', 'Manga'], dtype='object')
[5.9 5.1]
~~~

### Criar uma Series a partir de um dicionário
Nesse caso a chave é o índice.
~~~python
frutas = Series({'Uva': 5.90, 'Limão': 3.99, 'Manga': 5.10})
~~~

~~~python
print(frutas)



Uva      5.90
Limão    3.99
Manga    5.10
dtype: float64
~~~
