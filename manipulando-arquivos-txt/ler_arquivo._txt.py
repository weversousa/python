with open('manipulando-arquivos-txt/arquivo_criado.txt', 'r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê a primeira linha


with open('manipulando-arquivos-txt/arquivo_criado.txt', 'r', encoding='utf8') as arquivo:
    arquivo_completo_lista = arquivo.readlines()


arquivo = open('manipulando-arquivos-txt/arquivo_criado.txt', 'r', encoding='utf8')
trecho = arquivo.readline(3)  # lê os 3 primeiros caracter da primeira linha
print(trecho)
arquivo.close()
