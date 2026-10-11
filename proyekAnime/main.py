#program utama untuk menjalankan pengelolaan anime
from anime.fileio import siapkan_file, baca_anime
from anime.proses import anime, animeManager

siapkan_file() #memastikan file tersedia sebelum program berjalan
manager = animeManager() #membuat objek pengeloola anime

while True: #menampilkan menu pilahn user
    print('\nLIST NONTON ANIME')
    print('1. Tambah anime')
    print('2. Lihat daftar anime')
    print('3. Urutkan berdasarkan episode')
    print('4. Buat laporan')
    print('5. Keluar')

    try:
        pilih = int(input('Pilih menu: ')) #membaca menu piihan user

        if pilih == 1:
            judul = input('Judul anime: ')
            episode = int(input('Jumlah episode: '))
            status = input('Status: ')
            manager.tambah(anime(judul, episode, status))
            print('Anime berhasil ditambahkan.')

        elif pilih == 2:
            for anime in baca_anime():
                print(anime)

        elif pilih == 3:
            for anime in manager.urutkan():
                print(anime)

        elif pilih == 4:
            print(manager.laporan())
            print('Laporan tersimpan di laporan_anime.txt')

        elif pilih == 5:
            break

        else:
            print('Menu tidak tersedia.')

    except ValueError:
        print('Input episode tidak valid, harus berupa angka') #menangani input yang tidak falid
    except Exception as error:
        print('Terjadi kesalahan: ', error) #menampilkan kesalahan lain