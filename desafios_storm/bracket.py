"""Verifica se um brackte que abre tem um fechamento; balanceado ou não balanceado."""
from typing import List


def bracket_balanced(brackets: List[str]):
    """
    Pega um arquivo json com os brackets "({[]})" e verifica se são balanceadas {[}] Não balanceada {[]} Balanceada.

    :return: list
    """
    pilha = []
    for bracket in brackets:
        if bracket in ["(", "{", "["]:
            pilha.append(bracket)
        else:
            if not pilha:
                return False
            bracket_atual = pilha.pop()
            if bracket_atual == "(":
                if bracket != ")":
                    return False
            if bracket_atual == "{":
                if bracket != "}":
                    return False
            if bracket_atual == "[":
                if bracket != "]":
                    return False
    if pilha:
        return False
    return True
