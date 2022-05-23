# Biblioteca Data e Hora

https://docs.python.org/pt-br/3/library/datetime.html


## Classe date

A classe `date` pertence à biblioteca datetime e com ela podemos trabalhar com datas sem a hora.

*Entrada*:
~~~python
from datetime import date


data = date(year=1991, month=3, day=5)

print(data, type(data))

print(data.year, type(data.year))
print(data.month, type(data.month))
print(data.day, type(data.day))
~~~

*Saída*:
~~~python
1991-03-05 <class 'datetime.date'>

1991 <class 'int'>
3 <class 'int'>
5 <class 'int'>
~~~


### Função fromisoformat

O método `fromisoformat` pertence à classe date, recebe uma data no formato d etexto e seguindo o padrão ISO e também retorna um objeto do tipo date.

*Entrada*:
~~~python
from datetime import date


data = date.fromisoformat('1991-03-05')

print(data, type(data))
~~~

*Saída*:
~~~python
1991-03-05 <class 'datetime.date'>
~~~


### Função today

O método `today` pertence ao atributo date e retorna um objeto que contém a data atual do sistema.

*Exemplo*:
~~~python
from datetime import date


print(date.today())
~~~

*Saída*:
~~~python
2022-04-21
~~~


### Função replace

O método `replace` pertence ao atributo date e altera os valores da data.

*Saída*:
~~~python
from datetime import date


hoje = date.today()
print(hoje)

ano = hoje.year + 1
mes = hoje.month + 3
dia = hoje.day - 20

nova_data = hoje.replace(year=ano, month=mes, day=dia)
print(nova_data)
~~~

*Saída*:
~~~python
2022-04-21

2023-07-01
~~~


### Cálculo

*Exemplo*:
~~~python
from datetime import date


hoje = date.today()
print(hoje)

ano_novo = date(2022, 12, 31)
print(ano_novo)

dias = abs(ano_novo - hoje).days
print(f'Faltam {dias} para o Ano Novo.')
~~~

*Saída*:
~~~python
2022-04-21

2022-12-31

Faltam 254 para o Ano Novo.
~~~


### Função strftime

O método `strftime` pertence ao atributo date e formata as datas conforma os parâmetros passados.  
O seu retorno é do tipo texto.

*Saída*:
~~~python
from datetime import date


hoje = date.today()

print(hoje.strftime('%A %d %B %Y'))
print(hoje.strftime('%a %d %b %y'))
~~~

~~~
Thursday 21 April 2022
Thu 21 Apr 22
~~~


## Classe datetime

A classe `datetime` pertence à biblioteca datetime e com ela podemos trabalhar com datas e hora.

Caso a gente queira criar uma data é só passar os dados como parâmetro para a classe e ela vai retornar um objeto para ser trabalhado.

Por ser um objeto possui atributos, alguns são: year, month e day, ambos retornam um valor do tipo inteiro.

*Exemplo*:
~~~python
from datetime import datetime


data_hora = datetime(year=1991, month=3, day=5, hour=13, minute=49, second=59, microsecond=13)

print(data_hora, type(data_hora))

print(data_hora.year, type(data_hora.year))
print(data_hora.month, type(data_hora.month))
print(data_hora.day, type(data_hora.day))
print(data_hora.hour, type(data_hora.hour))
print(data_hora.minute, type(data_hora.minute))
print(data_hora.second, type(data_hora.second))
print(data_hora.microsecond, type(data_hora.microsecond))
~~~

*Saída*:
~~~python
1991-03-05 13:49:59.000013 <class 'datetime.datetime'>

1991 <class 'int'>
3 <class 'int'>
5 <class 'int'>
13 <class 'int'>
49 <class 'int'>
59 <class 'int'>
13 <class 'int'>
~~~


### Função fromisoformat

O método `fromisoformat` pertence à classe date e também retorna um objeto de data.


*Exemplo*:
~~~python
from datetime import date, datetime

data_hora = datetime.fromisoformat('1991-03-05 13:49:59:000013')

print(data_hora, type(data_hora))
~~~

*Saída*:
~~~python
1991-03-05 13:49:59.000013 <class 'datetime.datetime'>
~~~


### Função strptime

O método `strptime` pertence à classe datetime e também retorna um objeto de data.

Ele recebe 2 parâmetros, o 1º é a data em formato de texto e o 2º é o padrão de formatação seguindo a mesma ordem da tada.

*Exemplo*:
~~~python
from datetime import datetime


data_hora = datetime.strptime('05/03/1991 13:49:59:000013', '%d/%m/%Y %H:%M:%S:%f')

print(data_hora, type(data_hora))
~~~

*Saída*:
~~~python
1991-03-05 13:49:59.000013 <class 'datetime.datetime'>
~~~


### Função fromtimestamp

O método `fromtimestamp` pertence à classe datetime e também retorna um objeto de data.

O timestamp do unix corresponde ao número de segundos desde a meia-noite do dia 01/01/1970 no fuso horário UTC sem considerar os segundos bissextos.

*Exemplo*:
~~~python
from datetime import datetime


data_hora = datetime.fromtimestamp(1650565094.113016)

print(data_hora, type(data_hora))
~~~

*Saída*:
~~~python
2022-04-21 15:18:14.113016 <class 'datetime.datetime'>
~~~


### Função strftime

O método `strftime` pertence ao atributo datetime e formata as datas conforma os parâmetros passados.

*Saída*:
~~~python
from datetime import datetime


data_hora = datetime.now()
print(data_hora)

data_hora_formatado = data_hora.strftime('%d/%m/%Y %H:%M:%S')
print(data_hora_formatado, type(data_hora_formatado))
~~~

*Saída*:
~~~python
2022-04-21 13:01:21.437789

21/04/2022 13:01:21 <class 'str'>
~~~


### Função today

O método `today` pertence ao atributo datetime e retorna um objeto que contém a data atual do sistema.

*Exemplo*:
~~~python
from datetime import datetime


print(datetime.today())
~~~

*Saída*:
~~~python
2022-04-21 15:18:46.763927
~~~


### Função now

O método `now` pertence ao atributo datetime e retorna um objeto que contém a data e hora atuais do sistema.

O que o difere do método `today` é que ele pode receber um parâmetro par amudar o fuso horário.

*Exemplo*:
~~~python
from datetime import datetime


print(datetime.now())
~~~

*Saída*:
~~~python
2022-04-21 12:27:59.436637
~~~


### Fuso Horário

Trabalhando com servidores com o fuso horário diferente.

UTC (Coodinated Universal Time), o Tempo Universal Coordenado, é o fuso horário de referência a partir do qual se calculam todas as outras zonas horárias do mundo.

*Entrada*:
~~~python
from datetime import datetime


print(datetime.utcnow())
~~~

*Saída*:
~~~python
2022-04-21 17:15:32.975169
~~~


São Paulo tem uma diferença de -3h para o UTC, UTC-03:00.

*Entrada*:
~~~python
from datetime import datetime, timedelta, timezone


print(datetime.utcnow())

fuso_sp = timezone(timedelta(hours=-3))

print(datetime.now(fuso_sp))

data_hora = datetime.now()
data_hora = data_hora.astimezone(fuso_sp)
print(data_hora)
~~~

*Saída*:
~~~python
2022-04-21 17:15:32.975169

2022-04-21 14:15:32.975169-03:00

2022-04-21 14:15:32.975169-03:00
~~~


#### Função timezone

Trabalhando com Fuso Horário de forma mais automátca.

`pip install pytz`

*Exemplo*:
~~~python
from datetime import datetime

from pytz import timezone


print(datetime.utcnow())

print(datetime.now(timezone('America/Sao_Paulo')))
~~~

*Saída*:
~~~python
2022-04-21 17:15:32.975169

2022-04-21 14:15:32.975169-03:00
~~~


Relação de todos os Fusos Horários.

*Exemplo*:
~~~python
from pytz import all_timezones


for tz in all_timezones:
    print(tz)
~~~