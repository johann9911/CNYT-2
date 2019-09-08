import unittest
import math
import calculadoraC as ca

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
        self.assertEqual(ca.polarCartesianoC(3, 60), (1.5000000000000004, 2.598076211353316))
        self.assertEqual(ca.polarCartesianoC(5, 180), (-5.0, 6.123233995736766e-16))
        self.assertEqual(ca.polarCartesianoC(0, 30), 0)

    def test_cartesianoPolarC(self):
        self.assertEqual(ca.cartesianoPolarC(1, 1), (1.4142135623730951, 45.0))
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
        self.assertEqual(ca.sumaV([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)]), [(16, 0), (1, 1), (3, -9)])
        with self.assertRaises(ValueError):
            ca.sumaV([(1,0),(0,-1),(1,-1)],[(2,-2),(1,-1)])

    def test_inversaV(self):
        self.assertEqual(ca.inversaV([(1,2),(0,-2),(0,-3)]), [(-1, -2), (0, 2), (0, 3)])
        self.assertEqual(ca.inversaV([(1,0),(0,-1),(-3,1)]), [(-1, 0), (0, 1), (3, -1)])
        self.assertEqual(ca.inversaV([(-5,2),(3,0),(0,-1)]), [(5, -2), (-3, 0), (0, 1)])

    def test_productoCV(self):
        self.assertEqual(ca.productoCV((3,2),[(6,3),(0,0),(5,1),(4,0)]),[(12, 21), (0, 0), (13, 13), (12, 8)])
        self.assertEqual(ca.productoCV((8,-2),[(16,2.3),(0,-7),(6,0),(5,-4)]), [(132.6, -13.6), (-14, -56), (48, -12), (32, -42)])
        self.assertEqual(ca.productoCV((-1,1),[(-2,5),(-1,-1),(2,-9)]), [(-3, -7), (2, 0), (7, 11)])

    def test_normaV(self):
        self.assertEqual(ca.normaV([(2.6,2.7),(3.7,-6.4)]), 8.288546314040842)
        self.assertEqual(ca.normaV([(4,5),(3,1),(0,-7)]), 10)

    def test_distanciaMM(self):
        self.assertEqual(ca.distanciaV([(9,-7),(-1,-6)],[(7,-8),(5,-9)]), 7.0710678118654755)
        self.assertEqual(ca.distanciaV([(2,7),(4,-1),(2,-4)],[(7,8),(2,-8),(1,4)]), 12.0)

    def test_productoInternoVV(self):
        self.assertEqual(ca.productoInternoVV([(2,-1),(-8,-5),(-2,-6)],[(6,-3),(5,-1),(-6,-2)]), (4, 1))

    # Matrices
    def test_sumaM(self):
        self.assertEqual(ca.sumaM([[(1,0),(0,1)],[(0,1),(3,-4)],[(1,0),(-1,-1)]],[[(2,-1),(0,3)],[(0,-2),(5,0)],[(1,0),(0,-1)]]), [[(3, -1), (0, 4)],[(0, -1), (8, -4)], [(2, 0), (-1, -2)]])
        self.assertEqual(ca.sumaM([[(-8,-3),(-6,-4),(0,-4)],[(-1,8),(6,-10),(8,-5)],[(4,0),(8,5),(-7,-9)]],[[(-7,-2),(-4,-2),(7,7)],[(5,9),(0,3),(6,-5)],[(1,5),(-6,-6),(5,8)]]), [[(-15, -5), (-10, -6), (7, 3)], [(4, 17), (6, -7), (14, -10)], [(5, 5), (2, -1), (-2, -1)]])
        with self.assertRaises(ValueError):
            ca.sumaM([[(0,1),(3,-4)],[(1,0),(-1,-1)]],[[(2,-1),(0,3)],[(0,-2),(5,0)],[(1,0),(0,-1)]])

    def test_inversaM(self):
        self.assertEqual(ca.inversaM([[(1,-1),(0,1),(3,0)],[(5,-4),(6,7),(1,-1)],[(-1,0),(0,-1),(0,9)]]), [[(-1, 1), (0, -1), (-3, 0)], [(-5, 4), (-6, -7), (-1, 1)], [(1, 0), (0, 1), (0, -9)]])
        self.assertEqual(ca.inversaM([[(-3,1),(4,1)], [(-2,1),(2,1)],[(0,-1),(3,1)]]), [[(3, -1), (-4, -1)], [(2, -1), (-2, -1)], [(0, 1), (-3, -1)]])
        self.assertEqual(ca.inversaM([[(7,3),(-1,7)], [(-9,-4),(-7,-9)]]), [[(-7,-3),(1,-7)], [(9,4),(7,9)]])

    def test_productoCM(self):
        self.assertEqual(ca.productoCM((1,-1),[[(0,1),(-1,1)],[(2,1),(-1,2)]]), [[(1, 1), (0, 2)], [(3, -1), (1, 3)]])
        self.assertEqual(ca.productoCM((3,0),[[(1,-2),(-1,1)],[(-2,1),(-1,2)]]), [[(3, -6), (-3, 3)], [(-6, 3), (-3, 6)]])
        self.assertEqual(ca.productoCM((-2,3),[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]), [[(0,13), (-4, 32)], [(22, 32), (28, 10)]])

    def test_traspuestaM(self):
        self.assertEqual(ca.traspuestaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, -3), (0, 0), (1, 0)], [(2, 12), (5, 2.1), (2, 5)], [(0, -19), (17, 0), (3, -4.5)]])
        self.assertEqual(ca.traspuestaM([[1,2],[3,4]]), [[1, 3], [2, 4]])
        self.assertEqual(ca.traspuestaM([[(5,9),(-7,-5),(-1,-4)], [(8,2),(-3,-7),(7,-8)]]), [[(5, 9), (8, 2)], [(-7, -5), (-3, -7)], [(-1, -4), (7, -8)]])

    def test_conjugadaM(self):
        self.assertEqual(ca.conjugadaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, 3), (2, -12), (0, 19)], [(0, 0), (5, -2.1), (17, 0)], [(1, 0), (2, -5), (3, 4.5)]])
        self.assertEqual(ca.conjugadaM([[(1,2),(-3,5)],[(3,4),(-1,-1)]]), [[(1, -2), (-3, -5)], [(3, -4), (-1, 1)]])
        self.assertEqual(ca.conjugadaM([[(-6,1),(3,8)],[(2,-6),(3,0)]]), [[(-6, -1), (3, -8)], [(2, 6), (3, 0)]])

    def test_adjuntaM(self):
        self.assertEqual(ca.adjuntaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]), [[(6, 3), (0, 0), (1, 0)], [(2, -12), (5, -2.1), (2, -5)], [(0, 19), (17, 0), (3, 4.5)]])
        self.assertEqual(ca.adjuntaM([[(7,7),(3,8),(8,4)], [(5,0),(8,-6),(-10,-1)]]), [[(7, -7), (5, 0)], [(3, -8), (8, 6)], [(8, -4), (-10, 1)]])

    def test_isUnitaria(self):
        self.assertEqual(ca.isUnitaria([[(1,0),(0,0)],[(0,0),(1,0)]]), True)
        self.assertEqual(ca.isUnitaria([[(0,1),(1,0),(0,0)],[(0,0),(0,1),(1,0)],[(1,0),(0,0),(0,1)]]), False)
        self.assertEqual(ca.isUnitaria([[(1/math.sqrt(2),0),(0,1/math.sqrt(2))],[(0,1/math.sqrt(2)),(1/math.sqrt(2),0)]]), True)

    def test_isHermitiana(self):
        self.assertEqual(ca.isHermitiana([[(1,0),(3,-1)],[(3,1),(0,1)]]), False)
        self.assertEqual(ca.isHermitiana([[(3,0),(2,-1),(0,-3)],[(2,1),(0,0),(1,-1)],[(0,3),(1,1),(0,0)]]), True)

    def test_productoMM(self):
        self.assertEqual(ca.productoMM([[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]], [[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]), [[(-33, 153), (120, 0), (-44, -22)], [(87, 0), (-26, -117), (107, 70)], [(0, 165), (147, 26), (69, -36)]])
        with self.assertRaises(ValueError):
            ca.productoMM([[(2,1),(3,0),(1,-1)],[(0,0),(0,-2),(7,-3)],[(3,0),(0,0),(1,-2)]],[[(0,-1),(1,0)],[(0,0),(0,1)]])

    def test_accionMV(self):
        self.assertEqual(ca.accionMV([[(0,0),(0,-2)],[(0,2),(0,0)]],[(0,1),(1,0)]), [(0, -2), (-2, 0)])
        self.assertEqual(ca.accionMV([[(-1,5),(1,-7),(-6,3)],[(-3,-9),(2,-5),(1,-10)],[(-6,5),(6,-5),(3,-2)]],[(1,-3),(4,3),(-3,1)]), [(54, -32), (0, 17), (41, 30)])

if __name__ == '__main__':
    unittest.main()