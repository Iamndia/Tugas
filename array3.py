a = []
for i in range(10):
	artis = input("Masukkan nama artis = ")
	a.append(artis)
print(10*"=","Nama artis","="*10)
print("Nama artis = ",a)
a.remove(a[4])
a.remove(a[8])
print("Setelah dihapus = ",a)