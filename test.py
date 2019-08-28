import unittest
from T1 import calculadoraC as ca


class TestCal(unittest.TestCase):

    # Operaciones Basicas
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

    # Vectores
    def test_sumaV(self):
        self.assertEqual(ca.sumaV([(1,2),(0,-2),(0,-3)],[(2,3),(1,-1),(0,-4)]), [(3, 5), (1, -3), (0, -7)])
        self.assertEqual(ca.sumaV([(1,0),(0,-1),(1,-1)],[(2,-2),(1,-1),(4,-4)]), [(3, -2), (1, -2), (5, -5)])
        with self.assertRaises(ValueError):
            ca.sumaV([(1,0),(0,-1),(1,-1)],[(2,-2),(1,-1)])

    def test_inversaV(self):
        self.assertEqual(ca.inversaV([(1,2),(0,-2),(0,-3)]), [(-1, -2), (0, 2), (0, 3)])
        self.assertEqual(ca.inversaV([(1,0),(0,-1),(-3,1)]), [(-1, 0), (0, 1), (3, -1)])

    def test_productoV(self):
        self.assertEqual(ca.productoV((3,2),[(6,3),(0,0),(5,1),(4,0)]),[(12, 21), (0, 0), (13, 13), (12, 8)])
        self.assertEqual(ca.productoV((8,-2),[(16,2.3),(0,-7),(6,0),(5,-4)]), [(132.6, -13.6), (-14, -56), (48, -12), (32, -42)])

    # Matrices
    def test_sumaM(self):
        self.assertEqual(ca.sumaM([[(1,0),(0,1)],[(0,1),(3,-4)],[(1,0),(-1,-1)]],[[(2,-1),(0,3)],[(0,-2),(5,0)],[(1,0),(0,-1)]]), [[(3, -1), (0, 4)],[(0, -1), (8, -4)], [(2, 0), (-1, -2)]])
        with self.assertRaises(ValueError):
            ca.sumaM([[(0,1),(3,-4)],[(1,0),(-1,-1)]],[[(2,-1),(0,3)],[(0,-2),(5,0)],[(1,0),(0,-1)]])

    def test_inversaM(self):
        self.assertEqual(ca.inversaM([[(1,-1),(0,1),(3,0)],[(5,-4),(6,7),(1,-1)],[(-1,0),(0,-1),(0,9)]]), [[(-1, 1), (0, -1), (-3, 0)], [(-5, 4), (-6, -7), (-1, 1)], [(1, 0), (0, 1), (0, -9)]])
        self.assertEqual(ca.inversaM([[(-3,1),(4,1)], [(-2,1),(2,1)],[(0,-1),(3,1)]]), [[(3, -1), (-4, -1)], [(2, -1), (-2, -1)], [(0, 1), (-3, -1)]])

    def test_productoM(self):
        self.assertEqual(ca.productoM((1,-1),[[(0,1),(-1,1)],[(2,1),(-1,2)]]), [[(1, 1), (0, 2)], [(3, -1), (1, 3)]])
        self.assertEqual(ca.productoM((3,0),[[(1,-2),(-1,1)],[(-2,1),(-1,2)]]), [[(3, -6), (-3, 3)], [(-6, 3), (-3, 6)]])

    def test_traspuestaM(self):
        self.assertEqual(ca.traspuestaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, -3), (0, 0), (1, 0)], [(2, 12), (5, 2.1), (2, 5)], [(0, -19), (17, 0), (3, -4.5)]])
        self.assertEqual(ca.traspuestaM([[1,2],[3,4]]), [[1, 3], [2, 4]])

    def test_conjugadaM(self):
        self.assertEqual(ca.conjugadaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, 3), (2, -12), (0, 19)], [(0, 0), (5, -2.1), (17, 0)], [(1, 0), (2, -5), (3, 4.5)]])
        self.assertEqual(ca.conjugadaM([[(1,2),(-3,5)],[(3,4),(-1,-1)]]), [[(1, -2), (-3, -5)], [(3, -4), (-1, 1)]])

    def test_adjuntaM(self):
        self.assertEqual(ca.adjuntaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, 3), (0, 0), (1, 0)], [(2, -12), (5, -2.1), (2, -5)], [(0, 19), (17, 0), (3, 4.5)]])

if __name__ == '__main__':
    unittest.main()