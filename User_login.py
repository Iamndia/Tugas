"""
Perbandingan Logika dan Percabangan
No.1

"""
print(10*"=","LOGIN USER","="*10)
username = "Nadia"
password = "123"
username_input = input("Masukkan username Anda = ")
password_input = input("Masukkan password Anda = ")
if(username_input == username and password_input == password):
	print("Login sukses")
else:
	print("Login gagal")