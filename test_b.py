import unittest
from main import *

class TestFabrykaHulajnog(unittest.TestCase):

    def test_utworz_hulajnoge(self):
        fabryka = FabrykaHulajnog()

        hulajnoga_5km = fabryka.utworz_hulajnoge("5km")
        hulajnoga_10km = fabryka.utworz_hulajnoge("10km")
        hulajnoga_15km = fabryka.utworz_hulajnoge("15km")

        self.assertEqual(len(fabryka.produkty), 3)
        self.assertIn(hulajnoga_5km, fabryka.produkty)
        self.assertIn(hulajnoga_10km, fabryka.produkty)
        self.assertIn(hulajnoga_15km, fabryka.produkty)

        hulajnoga = fabryka.utworz_hulajnoge("20km")
        self.assertIsNone(hulajnoga)
        self.assertEqual(len(fabryka.produkty), 3)

if __name__ == '__main__':
    unittest.main()
