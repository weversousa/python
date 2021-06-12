''' Com o parâmetro w se o arquivo exitr será sobrescrito '''

with open('manipulando-arquivos-txt/arquivo_criado.txt', 'w', encoding='utf8') as f:
    f.writelines(['Arroz\n', 'Feijão\n', 'Café\n'])

    f.write('Miojo\n')
    f.write('Requeijão\n')

    print('Arquivo criado com sucesso.')
