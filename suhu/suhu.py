def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                hari, suhu = baris.strip().split(";")
                data.append({
                    "hari": hari,
                    "suhu": int(suhu)
                })
    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data

def kategori_suhu(suhu, batas=32):
    return "Panas" if suhu >= batas else "Normal"

def analisis_suhu(data, batas=32):
    if not data:
        return {
            "rata_rata": 0,
            "tertinggi": None,
            "terendah": None,
            "jumlah_panas": 0,
            "detail": []
        }

    rata_rata = sum(d["suhu"] for d in data) / len(data)
    tertinggi = max(data, key=lambda d: d["suhu"])
    terendah = min(data, key=lambda d: d["suhu"])

    detail = []
    for d in data:
        detail.append({
            "hari": d["hari"],
            "suhu": d["suhu"],
            "kategori": kategori_suhu(d["suhu"], batas)
        })

    jumlah_panas = sum(
        1 for d in detail if d["kategori"] == "Panas"
    )

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "detail": detail
    }

def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
    with open(nama_file, "w") as file:
        file.write(f"Rata-rata suhu: {hasil['rata_rata']:.2f}\n")

        if hasil["tertinggi"]:
            file.write(
                f"Suhu tertinggi: {hasil['tertinggi']['hari']} "
                f"({hasil['tertinggi']['suhu']} derajat)\n"
            )
            file.write(
                f"Suhu terendah: {hasil['terendah']['hari']} "
                f"({hasil['terendah']['suhu']} derajat)\n"
            )

        file.write(f"Jumlah hari panas: {hasil['jumlah_panas']}\n")
        file.write("\nDetail suhu harian:\n")

        for d in hasil["detail"]:
            file.write(
                f"{d['hari']}: {d['suhu']} - {d['kategori']}\n"
            )

    with open(nama_file, "r") as file:
        print(file.read())


if __name__ == "__main__":
    data = baca_data("suhu.txt")
    hasil = analisis_suhu(data)
    tulis_laporan(hasil)