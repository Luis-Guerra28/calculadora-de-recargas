import unittest
from main import combinaciones 

class TestCalculadora(unittest.TestCase):

    def test_valor_exacto_1(self):
        target = 100
        listValues = [50, 75, 100, 125, 150]
        result = combinaciones(target, listValues)
        self.assertEqual(result, [100, 100, [100], [100]])

    def test_valor_exacto_2(self):
        target = 80
        listValues = [20, 30, 40, 50, 60, 70, 80, 90]
        result = combinaciones(target, listValues)
        self.assertEqual(result, [80, 80, [80], [80]])

    def test_combinacion_exacta_1(self):
        target = 110
        listValues = [20, 30, 40, 50, 60, 70, 80, 90]
        result = combinaciones(target, listValues)
        
        self.assertEqual(
            [result[0], result[1], len(result[2]), len(result[3])],
            [110, 110, 2, 2]
        )

    def test_combinacion_exacta_2(self):
        target = 25
        listValues = [5, 10, 15, 20]
        result = combinaciones(target, listValues)
        
        self.assertEqual(
            [result[0], result[1], len(result[2]), len(result[3])],
            [25, 25, 2, 2]
        )


    def test_limites_diferentes_1(self):
        target = 120
        listValues = [50, 75, 100, 125, 150]
        result = combinaciones(target, listValues)
        self.assertEqual(result, [100, 125, [100], [125]])
    
    def test_limites_diferentes_2(self):
        target = 180
        listValues = [50, 75, 100, 125, 150]
        result = combinaciones(target, listValues)
        self.assertEqual(
            [result[0], result[1], len(result[2]), len(result[3])],
            [175, 200, 2, 2]
        )


if __name__ == '__main__':
    unittest.main()
