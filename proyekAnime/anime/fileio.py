FILE = 'list_anime.txt' #nama file
def siapkan_file():
    try:
        with open(FILE, 'x', encoding='utf-8') as f: #membuat file baru klo belum ada
            f.write("Naruto|220|Selesai\n")
    except FileExistsError: #agar ddata lama tidak tertimpa
        pass

def tambah_anime(judul, episode, status):
    with open(FILE, 'a', encoding='utf-8') as f: #menambahkan data baru
        f.write(f"{judul}|{episode}|{status}\n")

def baca_anime(): 
    data = [] #menampung data anime yang berhasil dibacaa
    try:
        with open(FILE, 'r', encoding='utf-8') as f: #membaca file secara bertahap
            for baris in f:
                try: 
                    judul, episode, status = baris.strip().split('|') #misahin judul, episode, dan status
                    data.append({
                        'judul': judul,
                        'episode': int(episode), #ngubah episode jadi bilanga bulat
                        'status': status
                    })
                except (ValueError, TypeError):
                    continue #melewati baris yang tidak valid
    except FileNotFoundError:
        print('File anime belum tersedia')
    return data
def simpan_laporan(teks):
    with open('laporan_anime.txt', 'w', encoding='utf-8') as f: #membuat atau menimpa file laporan
        f.write(teks)
