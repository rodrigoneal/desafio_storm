"""
Calcula o maximo de agua da chuva que pode ser armazenado entre duas elevações.

:author: Rodrigo Silva de Castro
:date:1/28/2021
"""


def amount_water(array):
    """
    Percorre a lista da esquerda pra direita e pega o maior valor do array no indice.

    N e armazena na variavel esquerda no indice N
    Percorre a lista da direita pra esquerda e pega o maior valor do array no indice
    N e armazena na variavel direita no indice N
    Pega o menor valor entre as  listas esquerda e direita no indice N e subtrai com o array no mesmo index esse valor
    é somado na variavel agua
    Exemplo: esquerda = 3; direita = 2; array = 1;
    primeiro você tira o menor valor que é 2
    logo 2 - 1 = 1
    1 é o valor que cabe de agua
    """
    tamanho = len(array)
    agua = 0
    # Cria duas listas com valores zero do tamanho da lista do array
    esquerda = tamanho * [0]
    direita = tamanho * [0]
    # Pega o primeiro valor do array
    esquerda[0] = array[0]
    # Declara que ele é o maior valor por enquanto
    max_esq = array[0]

    for index in range(0, tamanho):
        # Verifica se o maior valor do array no indece n é maior que o valor de max
        if max_esq < array[index]:
            # Atualiza o valor de max_esq com o maior valor do array no indice n
            max_esq = array[index]
            # Passa o maior valor para dentro da variavel esquerda
            esquerda[index] = max_esq
        else:
            # Se não houver um valor maior passa o valor anterior para o novo no indice n
            esquerda[index] = max_esq
    # Declara que o ultimo valor do array é o maior por enquanto
    max_dir = array[-1]
    # Pega os indeces de trás pra frente
    for index in range(tamanho - 1, -1, -1):
        # Se o max_dir é menor que o array com os indices de trás pra frente
        if max_dir < array[index]:
            max_dir = array[index]
            # Preenche a lista direita de trás pra frente
            direita[index] = max_dir

        else:
            direita[index] = max_dir

    for index in range(tamanho):
        agua += min(esquerda[index], direita[index]) - array[index]

    return agua


if __name__ == "__main__":
    a = amount_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(a)
