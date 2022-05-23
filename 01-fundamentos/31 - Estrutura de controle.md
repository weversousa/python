#

## Se, Senão Se, Senão

Quando queremos realizar uma série de verificações distintas.

*Exemplo*:
~~~python
nota = 2

if nota >= 6:
    print('Aprovado')
elif nota == 5:
    print('Recuperação')
else:
    print('Reprovado')
~~~

*Saída*:
~~~python
Reprovado
~~~

## Troca

Quando queremos comparar a mesma variável ou expressão com várias opções.

*Exemplo*:
~~~python
semana = 3

match semana:
    case 1:
        print('Domingo')
    case 2: 
        print('Segunda-feira')
    case 3: 
        print('Terça-feira')
    case 4: 
        print('Quarta-feira')
    case 5: 
        print('Quinta-feira')
    case 6: 
        print('Sexta-feira')
    case 7: 
        print('Sábado')
    case _:
        print('Semana inválida')
~~~

*Saída*:
~~~python
Terça-feira
~~~
