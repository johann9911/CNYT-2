import unittest
import calculadoraC as ca

class TestCal(unittest.TestCase):

    def test_sumaC(self):
        self.assertEqual(ca.sumaC(4,3,2,-4),(6,-1))
        self.assertEqual(ca.sumaC(2,2,1,5),(3,7))

    def test_restaC(self):
        self.assertEqual(ca.restaC(5,2,2,-1), (3, 3))
        self.assertEqual(ca.restaC(2,2,1,5), (1, -3))

    def test_productoC(self):
        self.assertEqual(ca.productoC(-3,3,1,-4), (9, 15))
        self.assertEqual(ca.productoC(4,3,2,-4), (20, -10))

    def test_divisionC(self):
        self.assertEqual(ca.divisionC(4,3,2,-4), (-4/20, 22/20))
        self.assertEqual(ca.divisionC(6,-6,6,-6), (1.0, 0.0))
        with self.assertRaises(ValueError):
            ca.divisionC(1,2,0,0)

    def test_polarCartesianoC(self):
        self.assertEqual(ca.polarCartesianoC(3, 60), (1.5, 2.6))
        self.assertEqual(ca.polarCartesianoC(5, 180), (-5.0, 0.0))
        self.assertEqual(ca.polarCartesianoC(0, 30), 0)

    def test_cartesianoPolarC(self):
        self.assertEqual(ca.cartesianoPolarC(1, 1), (1.41, 45.0))
        self.assertEqual(ca.cartesianoPolarC(-3, 0), (3, 180.0))

    def test_moduloC(self):
        self.assertEqual(ca.moduloC(4, 3), 5.0)
        self.assertEqual(ca.moduloC(10, -2), 10.2)

    def test_conjugadoC(self):
        self.assertEqual(ca.conjugadoC(4, 3), (4, -3))
        self.assertEqual(ca.conjugadoC(2, 3), (2, -3))

    def test_faseC(self):
        self.assertEqual(ca.faseC(1, -1), -45.0)
        self.assertEqual(ca.faseC(-1, 1), 135.0)

if __name__ == '__main__':
    unittest.main()