gaji = 5000000
alpa = int(input("Masukkan nilai = "))
potongan = 25000 * alpa
gaji_kotor =gaji- potongan
if(alpa > 3):
	gaji_bersih = gaji_kotor-(gaji_kotor * 5/100)
	print("potongan gaji = ",potongan)
	print("gaji setelah potongan = ",gaji_kotor)
	print("gaji bersih setelah pajak = ",gaji_bersih)
elif (alpa <= 3):
	gaji_bersih = gaji - (gaji * 5/100)
	print("gaji setelah pajak = ",gaji_bersih)
	