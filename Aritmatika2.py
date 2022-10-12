"""
Aritmatika 
No.2

"""
print('')
print(10*"=","MENGHITUNG HARGA JUAL TANAH","="*10)
panjang = int(input("Masukkan panjang tanah = "))
lebar     = int(input("Masukkan lebar tanah = "))
harga_tanah_per_meter = 500000
luas          = panjang * lebar
harga_jual = luas * harga_tanah_per_meter
print("Luas tanah = ",luas,"meter")

if(harga_jual > 500000):
	print("Harga jual = ",luas,"*",harga_tanah_per_meter,"=",harga_jual,"jt")
else:
	print("Harga jual =",luas,"*",harga_tanah_per_meter,"=",harga_jual,"rb")


