print(10*"=","Perulangan","="*10)
print("")
print("Bilangan genap yang dapat dibagi 5")
for i in range(1,100+1):
	if i % 2 == 0 and i % 5 == 0:
		print(i)
	else:
		print(end=' ')