"""
menghitung penghasilan zakat 

"""
penghasilan = int(input("Masukkan penghasilan = "))
min_zakat = 5240000
if(penghasilan >= min_zakat):
	print(penghasilan * 2,5 / 100)
else:
	print("Tidak terpenuhi")