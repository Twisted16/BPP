from funciones1 import calcula_media
import unittest

class Test_misfunciones1(unittest.TestCase):
    
    def setUp(self):
        print("Entrando en setup")
        
    def tearDown(self):
        print("Entrando en tearDown")
    
    
    
    def test_1(self):
        resul = calcula_media([100,0,50])
        self.assertEqual(resul,50)
    
    def test_2(self):
        resul2 = calcula_media([100,0,50])
        self.assertEqual(resul2,75)

    def test_3(self):
        resul3 = calcula_media([100,0,50])
        self.assertIn(resul3,[50])
    
    def test_4(self):
        resul4 = calcula_media([-1000,200,400,-200])
        self.assertEqual(resul4,-150)
    
    def test_5(self):
        resul5 = calcula_media([10,2])
        self.assertIn(resul5,[1,2,3,4,6,7,8,9,10])



if __name__ == '__main__':
    unittest.main()