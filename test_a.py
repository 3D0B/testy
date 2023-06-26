import unittest
from main import *

class test_a(unittest.TestCase):

    def test_hulajnoga_5km(self):
        hulajnoga = Hulajnoga5km("12345678")
        self.assertEqual(hulajnoga.wyswietl_informacje(), "Hulajnoga elektryczna 5km, kod modelu: 12345678")

    def test_hulajnoga_10km(self):
        hulajnoga = Hulajnoga10km("abcdefgh")
        self.assertEqual(hulajnoga.wyswietl_informacje(), "Hulajnoga elektryczna 10km, kod modelu: abcdefgh")

    def test_hulajnoga_15km(self):
        hulajnoga = Hulajnoga15km("ijklmnop")
        self.assertEqual(hulajnoga.wyswietl_informacje(), "Hulajnoga elektryczna 15km, kod modelu: ijklmnop")

    def test_utworz_hulajnoge_5km(self):
        fabryka = FabrykaHulajnog()
        hulajnoga = fabryka.utworz_hulajnoge("5km")
        self.assertIsInstance(hulajnoga, Hulajnoga5km)
        self.assertIn(hulajnoga, fabryka.produkty)

    def test_utworz_hulajnoge_10km(self):
        fabryka = FabrykaHulajnog()
        hulajnoga = fabryka.utworz_hulajnoge("10km")
        self.assertIsInstance(hulajnoga, Hulajnoga10km)
        self.assertIn(hulajnoga, fabryka.produkty)

    def test_utworz_hulajnoge_15km(self):
        fabryka = FabrykaHulajnog()
        hulajnoga = fabryka.utworz_hulajnoge("15km")
        self.assertIsInstance(hulajnoga, Hulajnoga15km)
        self.assertIn(hulajnoga, fabryka.produkty)

    def test_utworz_hulajnoge_nieznany_typ(self):
        fabryka = FabrykaHulajnog()
        hulajnoga = fabryka.utworz_hulajnoge("20km")
        self.assertIsNone(hulajnoga)
        self.assertEqual(len(fabryka.produkty), 0)

if __name__ == '__main__':
    unittest.main()
