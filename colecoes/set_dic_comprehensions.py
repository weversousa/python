from collections import Counter

with open('texto.txt', 'r') as t:
    texto = t.read()


def exemplo_1(texto):
    letras = []
    quantidade = []
    for letra in texto:
        if letra not in letras:
            letras.append(letra)
            quantidade.append(1)
        else:
            indice = letras.index(letra)
            quantidade[indice] += 1
    dicionario = {}
    for indice in range(len(letras)):
        dicionario[letras[indice]] = quantidade[indice]
    print(dicionario)


def exemplo_2(texto):
    letras = set()
    for letra in texto:
        letras.add(letra)
    letras = list(letras)
    quantidade = [texto.count(letra) for letra in letras]
    dicionario = {}
    for indice in range(len(letras)):
        dicionario[letras[indice]] = quantidade[indice]
    print(dicionario)


def exemplo_3(texto):
    letras = list({letra for letra in texto})
    quantidade = [texto.count(letra) for letra in letras]
    dicionario = {}
    for indice in range(len(letras)):
        dicionario[letras[indice]] = quantidade[indice]
    print(dicionario)


def exemplo_4(texto):
    letras = list({letra for letra in texto})
    quantidade = [(letra, texto.count(letra)) for letra in letras]
    print(dict(quantidade))


def exemplo_5(texto):
    quantidade = [(letra, texto.count(letra)) for letra in set(texto)]
    print(dict(quantidade))


def exemplo_6(texto):
    print(dict([(letra, texto.count(letra)) for letra in set(texto)]))


def exemplo_7(texto):
    print({letra: texto.count(letra) for letra in set(texto)})


def exemplo_8(texto):
    print(Counter(texto))
    print(Counter(texto).most_common(4))  # Os 4 mais frequentes


exemplo_8(texto)
