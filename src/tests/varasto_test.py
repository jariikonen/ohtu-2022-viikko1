import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_varaston_tilavuus_nolla(self):
        varasto2 = Varasto(0)
        self.assertAlmostEqual(varasto2.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto3 = Varasto(10, -1)
        self.assertAlmostEqual(varasto3.saldo, 0)

    def test_tilavuutta_suurempi_alkusaldo(self):
        varasto4 = Varasto(10, 11)
        self.assertAlmostEqual(varasto4.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tilavuutta_suurempi_lisays_ei_kasvata_saldoa_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_antaa_nolla(self):
        saatu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu, 0)

    def test_saldoa_suurempi_ottaminen_antaa_saldon_verran(self):
        saldo = 5
        self.varasto.lisaa_varastoon(saldo)
        saatu = self.varasto.ota_varastosta(15)
        self.assertAlmostEqual(saatu, saldo)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_antaa_oikean_merkkijonon(self):
        saldo = 5
        self.varasto.lisaa_varastoon(saldo)
        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 5")
