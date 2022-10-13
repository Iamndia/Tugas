a = []
nilai = int(input("Masukkan berapa nilai = "))
for i in range(nilai):
	artis = input("Masukkan nilainya = ")
	a.append(artis)
print(10*"=","OUTPUT","="*10)
print("nilai = ",a)
print("Nilai terbesar = ",max(a))
print("Nilai terkecil = ",min(a))