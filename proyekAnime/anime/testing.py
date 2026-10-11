# Pengujian otomatis menggunakan library unittest.
import unittest
from .proses import anime, animeManager
from .validasi import DataAnimeError


class TestAnime(unittest.TestCase):
    #menguji pembuatan objek anime.
    def test_anime(self):
        self.assertEqual(anime('One Piece', 100).episode, 100)

    #menguji penolakan judul kosong.
    def test_judul_kosong(self):
        with self.assertRaises(DataAnimeError):
            anime('', 10)

    #menguji penolakan episode negatif.
    def test_episode_negatif(self):
        with self.assertRaises(DataAnimeError):
            anime('Bleach', -1)

    # menguji perhitungan total episode.
    def test_total_episode(self):
        self.assertEqual(animeManager().total_episode(10, 20, 30), 60)

    #menguji pembuatan record menggunakan kwargs.
    def test_record(self):
        data = animeManager().buat_record(judul='Naruto', episode=220)
        self.assertEqual(data['judul'], 'Naruto')

#menjalankan pengujian saat modul dipanggil
if __name__ == '__main__':
    unittest.main()