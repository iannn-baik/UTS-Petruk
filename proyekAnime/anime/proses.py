#mengimpor fungsi pengelolaan file dan validasi
from .fileio import baca_anime, tambah_anime, simpan_laporan
from .validasi import validasi_anime

#menyimpan informasi satu anime
class anime:
    def __init__(self, judul, episode, status='Belum selesai'):
        validasi_anime(judul, episode) #memvalidasi data sebelum disimpan
        self.judul = judul #nyimpen atribut animme
        self.episode = episode
        self.status = status

    def record(self): #mengubah atribut objek menjadi dictionary
        return vars(self)

#mengelola daftar anime dan laporan
class animeManager:
    def tambah(self, anime): #menyimpan anime dengan keyword argument
        tambah_anime(
            judul=anime.judul,
            episode=anime.episode,
            status=anime.status
        )

    def total_episode(self, *angka): #menjumlahkan beberapa angka
         return sum(angka)

    def buat_record(self, **kwargs): #mmembuat record dengan atribut yang fleksibel
        return kwargs

    def urutkan(self): #ngurutin anime dari jumlah episode
        return sorted(
            baca_anime(),
            key=lambda data: data['episode']
        )

    def analisis(self): #membaca seluruh data untuk dianalisis
        data = baca_anime()

        assert all(anime['episode'] >= 0 for anime in data) #memastikan jumlah episode tidak negatif

        total = self.total_episode(
            *(anime['episode'] for anime in data)
        )
#membuat bagian awal laporan
        teks = 'LAPORAN LIST NONTON ANIME\n'
        teks += f'Jumlah anime: {len(data)}\n'
        teks += f'Total episode: {total}\n\n'
        teks += 'Daftar Anime:\n'
#nulis data anime satu persatu
        for nomor, anime in enumerate(data, start=1):
            teks += (
                f'{nomor}. {anime["judul"]} - '
                f'{anime["episode"]} episode - '
                f'{anime["status"]}\n'
            )

        return teks
#membuat laporan, menyimpan lalu mengembalikkan hasil
    def laporan(self):
        teks = self.analisis()
        simpan_laporan(teks)
        return teks