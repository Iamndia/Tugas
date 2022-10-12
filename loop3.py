print(10*"=","Perulangan","="*10)
print("")
print("Bilangan genap yang habis dibagi 3")
for i in range(1,100+1):
	if i % 2 == 0 and i % 3 == 0:
		print(i)
	else:
		print(end=' ')