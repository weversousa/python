*Exemplo*:
~~~python
from typing import List, Tuple, Dict, Any


produto_id: int = 1
produto_nome: str = 'TV LG 40º'
produto_preco: float = 2_429.99
produto_desconto: bool = False

numeros: List[int] = [1, 2, 3]
nomes: Tuple[str] = ('Weverton', 'Ana', 'Júlia')
estados: Dict[int, str] = {1: 'São Paulo', 2: 'Bahia'}

heterogenea: List[Any] = [1, 6.9, 'Ana', True, ('x', 'y'), {'a': 'b'}, [3, 8]]

produtos: List[Tuple[int, str, float, bool]] = [
    (1, 'TV LG 40º', 2_429.99, False),
    (2, 'Celular Samsung', 1_700.99, True)
]


def somar(n1: int = 0, n2: int = 0) -> int:
    return n1 + n2

def saudacao(nome: str = 'cliente',) -> None:
    print('Olá, senhor (a) ', nome, '.')
~~~