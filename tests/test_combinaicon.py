import unittest
from main import combinaciones 

class TestCalculadora(unittest.TestCase):

    def test_valor_exacto(self):
        target = 100
        listValues = [50, 75, 100, 125, 150]

        result = combinaciones(listValues, target)

        self.assertEqual(result, [100, 100, [100], [100]])

if __name__ == '__main__':
    unittest.main()
