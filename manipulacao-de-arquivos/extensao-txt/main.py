# Em Python, uma operação de arquivo ocorre na seguinte ordem:
# 1. Abra um arquivo
# 2. Ler ou escrever (executar operação)
# 3. Feche o arquivo


# Criando arquivos.  Para isso o mode deve ser W.
# Usamos a função open, se não existir o arquivo é criado
try:
    caminho_do_arquivo = 'manipulacao_de-arquivos/extensao-txt/jogadores.txt'
    arquivo = open(file=caminho_do_arquivo, mode='w', encoding='utf-8')
    arquivo.write('Nome,Clube\n')
    arquivo.write('C. Ronaldo,Juventus\n')
    arquivo.write('Messi,Barcelona\n')
    arquivo.write('Neymar,PSG\n')
finally:
    arquivo.close()

# -----------------------------------------------------------------------------

# Lendo arquivo. Para isso o mode deve ser R.
# No lugar do try e  finally é melhor usar with, ele fecha o arquivo
# automaticamente após o uso dele.
with open(file=caminho_do_arquivo, mode='r', encoding='utf-8') as arquivo:

    # Para especificar quantos caractres ler.
    valor = arquivo.read(5)
    print(valor)

    # Ao chamar novamente na mesma execução ele continua de onde parou.
    valor = arquivo.read(10)
    print(valor)

    # Sem passar parâmetros ele trás tudo "de onde parou da última vez".
    # Se for a primeira execução vai trazer o aquivo todo.
    valor = arquivo.read()
    print(valor)

# Resultado:
# Nome,
# Clube
# C. R
# onaldo,Juventus
# Messi,Barcelona
# Neymar,PSG
# -----------------------------------------------------------------------------

print('-' * 20)

with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:

    for linha in arquivo:
        # Como já tem o \n no arquivo tiramos a quebra do print
        print(linha, end='')

# Resultado
# Nome,Clube
# C. Ronaldo,Juventus
# Messi,Barcelona
# Neymar,PSG
# -----------------------------------------------------------------------------

print('-' * 20)

with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:

    texto = arquivo.readline()

    while texto != '':
        print(texto, end='')
        texto = arquivo.readline()

# Resultado
# Nome,Clube
# C. Ronaldo,Juventus
# Messi,Barcelona
# Neymar,PSG
# -----------------------------------------------------------------------------

print('-' * 20)

# Retorna uma lista com cada elemento sendo uma linha do arquivo.
with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:

    texto_em_lista = arquivo.readlines()

    print(texto_em_lista)

# Resultado:
# ['Nome,Clube\n', 'C. Ronaldo,Juventus\n', 'Messi,Barcelona\n', 'Neymar,PSG\n']
