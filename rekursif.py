a = []
nilai = int(input("Masukkan berapa nilai = "))
for i in range(nilai):
	jumlah = input("Masukkan nilainya = ")
	a.append(jumlah)
print(10*"=","OUTPUT","="*10)
print("nilai = ",a)
print("Nilai terbesar = ",max(a))
print("Nilai terkecil = ",min(a))