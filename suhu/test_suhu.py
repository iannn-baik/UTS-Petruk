import unittest
from suhu import kategori_suhu, analisis_suhu

class TestSuhu(unittest.TestCase):

    def test_kategori_panas(self):
        self.assertEqual(kategori_suhu(32), "Panas")
    def test_kategori_normal(self):
        self.assertEqual(kategori_suhu(30), "Normal")
    def test_analisis_suhu(self):
        data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28}
        ]

        hasil = analisis_suhu(data)
        self.assertAlmostEqual(hasil["rata_rata"], 31.142857142857142)
        self.assertEqual(hasil["tertinggi"]["suhu"], 35)
        self.assertEqual(hasil["terendah"]["suhu"], 28)
        self.assertEqual(hasil["jumlah_panas"], 3)

if __name__ == "__main__":
    unittest.main()