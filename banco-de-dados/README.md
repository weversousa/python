## Tipos de dados

# Data Type | Range  | Storage
CHAR(n)     | 1-8000 | n bytes
VARCHAR(n)  | 1-8000 | n + 2 bytes

CHAR(n) -> Usar esse quando não tem variação de tamanho ou muito pouca variação
se você estipular CHAR(100), mesmo que uma das informações tenha 10 caracteres
ele vai consumir 100 bytes.

VARCHAR(n) Usar esse quando os tamanhos de dados variam muito de tamnaho. Esse
tipo faz com que a coluna use somente o tamanho do dado + 2 bytes.


## Restrições CONSTRAINTS são 5

Chave Primaria (PRIMARY KEY) -> pk
Chave Estrangeira (FOREGEIN KEY) -> fk
Chave Única (Chave Candidata ou Chave Alternativa) -> uq
Padrão (DEFALUT) -> df
Checar (CHECK) -> ck

ALTER TABLE <nome da tabela> ADD <nome da coluna> <tipo de dados>
ALTER TABLE <nome da tabela> ADD CONSTRAINT <nome da coluna> <tipo de dados>
ALTER TABLE <nome da tabela> ALTER COLUMN <nome da coluna> <tipo de dados>
ALTER TABLE <nome da tabela> DROP COLUMN <nome da coluna>
ALTER TABLE <nome da tabela> DROP CONSTRAINT <nome da coluna>

DROP TABLE <nome da tabela 1>, <nome da tabela 2>

TRUNCATE TABLE <nome da tabela>
Não funciona em tabela ocm chave estrangeira

DELETE TABLE <nome da tabela>


UPDATE <nome da tabela>
SET <nome da coluna> = <expressão>
WHERE <condição>


sp_help <nome tabel>

SELECT <nomes colunas>
INTO <nova tabela>
FROM <nome tabela>
WHERE <condicao>