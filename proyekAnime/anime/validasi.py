#Exception khusus untk menangani data yang tidak valid
class DataAnimeError(Exception):
    pass
#memeriksa judul dan jumlah epidsode sebelum di proses
def validasi_anime(judul, episode):
    if not judul.strip() or episode < 0:
        raise DataAnimeError('judul kosong atau episode anime tidak boleh negatif.')
    #judul tidak boleh kosong dan episode tidak boleh negatif
    return True
#mengembalikan True jika data valid
    