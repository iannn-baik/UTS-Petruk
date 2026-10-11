def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)

def tentukan_status(rata_rata, batas_lulus=70):
    return 'Lulus' if rata_rata >= batas_lulus else 'Tidak Lulus'

def hitung_nilai(nama, daftar_nilai, batas_lulus=70):
    nilai =[float(n) for n in daftar_nilai]
    rata_rata = hitung_rata_rata(nilai)
    status = tentukan_status(rata_rata, batas_lulus)

    print(f'Nama: {nama}')
    print(f'Rata-rata: {rata_rata}')
    print(f'Status: {status}')

if __name__ == '__main__':
    hitung_nilai('Budi', [80, 75, 90])
    hitung_nilai('Sari', [60, 65, 55,70])