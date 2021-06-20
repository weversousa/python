from datetime import datetime as dt

data_atual = dt.now()

data_string = '2021-06-08 21:21:00'

data_objeto = dt.strptime(data_string, '%Y-%m-%d %H:%M:%S')

