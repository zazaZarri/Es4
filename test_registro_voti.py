import unittest
from registro_voti import RegistroVoti


class TestRegistroVoti(unittest.TestCase):
    def setUp(self):
        self.registro = RegistroVoti()

    def test_media_registro_vuoto(self):
        self.assertEqual(self.registro.calcola_media(), 0.0)

    def test_media_voti_validi(self):
        for voto in (8, 7, 9):
            self.registro.aggiungi_voto(voto)
        self.assertAlmostEqual(self.registro.calcola_media(), 8.0)

    def test_voto_valido_viene_aggiunto(self):
        self.registro.aggiungi_voto(6)
        self.assertEqual(self.registro.voti, [6])

    def test_voto_fuori_intervallo_ignorato(self):
        self.registro.aggiungi_voto(11)
        self.registro.aggiungi_voto(-1)
        self.assertEqual(self.registro.voti, [])

    def test_estremi_accettati(self):
        self.registro.aggiungi_voto(0)
        self.registro.aggiungi_voto(10)
        self.assertEqual(self.registro.voti, [0, 10])


if __name__ == "__main__":
    unittest.main()