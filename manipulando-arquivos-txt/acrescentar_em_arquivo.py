''' Com o parâmetro a não apaga nada, escreve no fim '''

with open('manipulando-arquivos-txt/arquivo_criado.txt', 'a', encoding='utf8') as f:
    f.writelines(['Laranjca\n', 'Ovo\n', 'Azeite\n'])
