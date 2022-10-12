"""
Buatlah beberapa variabel yang masing-masing dapat menampung nama depan(String),nama belakang(String),umur (integer),tinggi(satuan meter)(float,dooble),berat badan(satuan kg/float/dooble),ukuran baju(S,M,atau L)(char),dan status pernikahan (boolean),kemudian berikan nilai/value kepada setiap variabel dan tampilkan nilai setiap variabel tersebut.

"""
namaDepan = "Nadia"
namaBelakang = " TI"
umur = 18
tinggi = 1.48
beratBadan = 37
ukuranBaju = 'L'
status_pernikahan = False

print(8*"=","OUTPUT","="*8)
print("Nama = ",namaDepan + namaBelakang)
print("Umur = ",umur)
print("Tinggi = ",tinggi)
print("Berat badan = ",beratBadan)
print("Ukuran Baju = ",ukuranBaju)
print("Status Pernikahan = ",status_pernikahan)

#mengetahui tipe data
print("")
print("Nama depan = ",type(namaDepan))
print("Nama belakang = ",type(namaBelakang))
print("Umur  = ",type(umur))
print("Tinggi = ",type(tinggi))
print("Berat Badan = ",type(beratBadan))
print("Ukuran  = ",type(ukuranBaju))
print("Status pernikahan = ",type(status_pernikahan))

"""
pada variabel ukuran baju saya tidak menggunakan tipe data char karena saya tidak tau cara menggunakannya

"""