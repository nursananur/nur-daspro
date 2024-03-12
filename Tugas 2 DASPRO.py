def gajiperminggu(gajibulan):
    return round (gajibulan / 4.33)

def gajiperhari(gajiperminggu, jumlahhari):
    return round (gajiperminggu / jumlahhari)

def gajiperjam(gajiperhari, jamkerja):
    return round (gajiperhari / jamkerja)

gajibulan = float(input("Masukkan gaji per bulan anda: "))
jamkerja = int(input("Masukkan jumlah jam kerja per hari: "))
jumlahhari = int(input("Masukkan jumlah hari kerja per minggu: "))

gaji_per_minggu = gajiperminggu(gajibulan)
gaji_per_hari = gajiperhari(gaji_per_minggu, jumlahhari)
gaji_per_jam = gajiperjam(gaji_per_hari, jamkerja)

print("== Nursan Anur==")
print("== 07352311123==")
print(f"Gaji per minggu: {gaji_per_minggu}"' ' "rupiah")
print(f"Gaji per hari: {gaji_per_hari}"' ' "rupiah")
print(f"Gaji per jam: {gaji_per_jam}"' '"rupiah")
