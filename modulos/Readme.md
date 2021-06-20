# Módulo Principal

O '__main__' contém o nome do módulo (arquivo) que tal objeto pertence

Se eu perguntar se '__main__' == __name__ no próprio aquivo é True

Mas se eu colocar essa condição em uma função de outro arquivo, importar
esse arquivo e executar essa função a comparação é False.
Pois o arquivo está o executando é diferente do arquivo dono da função.
