# Aplicação com assert, usado para verificar se o (sum) funciona da forma esperada.
def sum_numbers(numbers):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0

    return sum(numbers)

teste = sum_numbers([1, 2, 3, 5])  
print(teste)

# O doctest lê os exemplos e executa, conferindo se a saída bate.
def sum_numbers(numbers):
    """
    Soma os números em uma lista.

    Exemplos:
    >>> sum_numbers([1, 2, 3, 4])
    10
    >>> sum_numbers([-1, 0, 1])
    0
    >>> sum_numbers([])
    0
    """
    return sum(numbers)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#

import unittest

def sum_numbers(numbers):
    return sum(numbers)

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_sum_numbers_mixed(self):
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
