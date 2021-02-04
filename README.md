# DESAFIO STORM

[![Build Status](https://travis-ci.com/rodrigoneal/desafio_storm.svg?branch=master)](https://travis-ci.com/rodrigoneal/desafio_storm)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c0c887dea1648b2973cc2d541126edb)](https://www.codacy.com/gh/rodrigoneal/desafio_storm/dashboard?utm_source=github.com&utm_medium=referral&utm_content=rodrigoneal/desafio_storm&utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/1c0c887dea1648b2973cc2d541126edb)](https://www.codacy.com/gh/rodrigoneal/desafio_storm/dashboard?utm_source=github.com&utm_medium=referral&utm_content=rodrigoneal/desafio_storm&utm_campaign=Badge_Coverage)

## Como usar

---

### Instalação

`pip install git+https://github.com/rodrigoneal/desafio_storm`

### Importando e usando

##### index_value(nums: List[int], alvo: int)

Função que soma os valores da lista e retorna o indice dos valores que somados são
iguais ao valor de alvo. <br />

Retorna:List. Se o valor de alguma das somas for igual a alvo<br /> Retorna: None. Se o
valor de nenhuma das somas for igual a alvo.

**Argumento** nums: tipo: list. Lista de números inteiros que serão somadas para
encontrar o valor de alvo.

**Argumento** alvo: tipo: int. O número pelo qual será dado o indice das somatorias.

Todos argumentos são posicionais.

`from desafios_storm.index import index_value`

`index = index_value([2, 7, 11, 15], 9)` <br /> `print(index)`

`>>> [0, 1]`

#### bracket_balanced(brackets: List[str])

Função que procura se uma expressão é balanceada. Se todos os brackets abertos tem o seu
par de fechamento na ordem certa.

Retorna um booleano. <br /> Se balanceada retorna `True` <br /> Se não balanceada
retorna `False`

**Argumento** alvo: tipo: list. Uma lista de string com a expressão que será analisada

`from desafios_storm.bracket import bracket_balanced`

`is_balanced = bracket_balanced('{{}}')`

`print(is_balanced)`

`>>> True`

#### amount_water(array: List[int])

Função que calcula a quantidade de agua que um mapa de elevação pode reter.

**Argumento** array:tipo: list. Lista com os valores inteiros com o mapa de elevação.

`from desafios_storm.water import amount_water`

`water = amount_water([0,1,0,2,1,0,1,3,2,1,2,1])` <br /> `print(water)`

`>>> 6`

# Notas de desenvolvimento.

Eu não consegui fazer o desafio 3 pois não conseguir entender a questão.

A princípio fiz uma API. Pois, pra mim, fazia mais sentido para a vaga de backend, mas
conversando com a Tânia(RH), ela explicou-me que eu deveria focar no condigo. Por isso
resolver refazer só com funções pra ficar mais legivel. Mas em todo caso deixei a API no
meu GitHub, mas não tornei instalável, se desejar posso seguir com o outro projeto.

Foram escrito 6 testes que podem ser testado com o comando <br />
`python -m unittest desafios_storm.test.test_desafios`
