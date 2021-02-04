"""
Recebe um array de valores e um valor alvo e calcula se a soma de algum dos valores dentro do array for igual ao alvo retorna o indice dos dois numeros.

author: Rodrigo Silva de Castro
date:1/28/2021
"""
from typing import List


def index_value(nums: List[int], alvo: int):
    """Recebe uma lista e um numeros de alvo que calcula os valores retornao indice dos valores que se somam."""
    for i in range(len(nums)):
        # Pula o valor de i pra não gerar soma por ele mesmo
        for v in range(i + 1, len(nums)):
            # Verifica se o index de nums no index i e v == alvo
            if nums[i] + nums[v] == alvo:
                return [i, v]


if __name__ == "__main__":
    a = index_value([2, 7, 11, 15], 9)
    print(a)
