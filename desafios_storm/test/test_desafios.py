"""Pacote de teste."""

import unittest

from desafios_storm.water import amount_water
from desafios_storm.index import index_value
from desafios_storm.bracket import bracket_balanced


class Test_desafios_storm(unittest.TestCase):
    """Classe usada pelo unittest."""

    def test_if_index_value_retorna_0_1(self):
        """Testa a funcao index_value retorna [0,1]."""
        nums = [2, 7, 11, 15]
        alvo = 9
        self.assertEqual(index_value(nums, alvo), [0, 1])

    def test_if_index_value_retorna_1_3(self):
        """Testa a funcao index_value retorna [1,3]."""
        nums = [2, 7, 11, 15]
        alvo = 22
        self.assertEqual(index_value(nums, alvo), [1, 3])

    def test_if_index_value_retorna_None(self):
        """Testa a funcao index_value retorna None."""
        nums = [2, 7, 11, 15]
        alvo = 23
        self.assertEqual(index_value(nums, alvo), None)

    def test_se_bracket_balanced_retorna_true(self):
        """Testa se a funcao bracket_balanced retorna True."""
        bracket = "{[()]}"
        self.assertEqual(bracket_balanced(bracket), True)

    def test_se_bracket_balanced_retorna_false(self):
        """Testa se a funcao bracket_balanced retorna False."""
        bracket = "{[(])}"
        self.assertEqual(bracket_balanced(bracket), False)

    def test_se_amount_water_retorna_6(self):
        """Testa se a funcao amount_water retorna o 6."""
        elevacao = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(amount_water(elevacao), 6)


if __name__ == "__main__":
    unittest.main()
