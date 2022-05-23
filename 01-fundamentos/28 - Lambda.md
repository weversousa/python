# Lambda

A lambda é uma função para resoluções curtas. Ela pode ser armazenada em uma variável ou invocada em tempo de execução.

Sintaxe: `lambda parametros: retorno`

Se tiver mais de um parâmetro é só separar por `,`.

*Exemplo*:
~~~python
campeao = lambda times: times[0]
print(campeao(['São Paulo', 'Vasco', 'Corinthians']))
~~~

*Saída*:
~~~python
São Paulo
~~~

*Exemplo*:
~~~python
soma = lambda n1, n2: n1 + n2
print(soma(3, 4))
~~~

*Saída*:
~~~python
7
~~~

Muitos métodos em Python pedem como parãmetro um iterável e uma função para tratar os dados desse iterável.

Nesses casos podemos passar tanto a função `lambda` direto sem armazenar em uma variável como também podemos passar a função tradiconal `def`.