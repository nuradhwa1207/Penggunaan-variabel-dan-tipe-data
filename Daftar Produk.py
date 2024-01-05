# Membuat daftar produk, merek, dan harga
# string
produk = ["Kipas angin", "Helem", "Setrika","Sandal"]
merek = ["Mikako", "Monda", "Kaspion", "Sulow" ]
harga = [82000, 140000, 95000, 9000]

# Menggabungkan data dalam daftar-daftar ke dalam satu daftar
daftar_produk = list(zip(produk, merek, harga))

# Menampilkan daftar produk
for item in daftar_produk:
    print(f"Produk: {item[0]}, Merek: {item[1]}, Harga: Rp. {item[2]}")