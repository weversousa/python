with open('txt/arquivo_criado.txt', 'r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê a primeira linha
    print(linha)


with open('txt/arquivo_criado.txt', 'r', encoding='utf8') as arquivo:
    arquivo_completo_lista = arquivo.readlines()
    print(arquivo_completo_lista)


arquivo = open('txt/arquivo_criado.txt', 'r', encoding='utf8')
trecho = arquivo.readline(3)  # lê os 3 primeiros caracter da primeira linha
print(trecho)
arquivo.close()
