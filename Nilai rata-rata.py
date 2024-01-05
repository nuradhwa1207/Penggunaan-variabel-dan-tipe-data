# Program untuk menghitung  hasil rata-rata Nilai Tugas, UTS dan UAS mata kuliah.
# float
tugas = float(input("Masukan nilai tugas :"))
uts = float(input("Masukan nilai UTS :"))
uas = float(input("Masukan nilai UAS :"))

# Menghitung hasil rata-rata
rata_rata = (tugas+uts+uas)/3

# Menampilkan hasil rata-rata
print("Hasil rata-rata :", rata_rata)