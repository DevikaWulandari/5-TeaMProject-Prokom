import csv



def registrasi():
    with open('username.csv', 'a') as f:
        writer = csv.writer(f)
        user = input("Username : ")
        pw = input("Password : ")
        writer.writerow([user,pw])
        print("\nSilahkan Login")
        login()

def login():
    user = input("Username : ")
    pw = input("Password : ")
    with open("username.csv", "r") as x:
        reader = csv.reader(x, delimiter=",")
        for row in reader:
            if row == ([user,pw]):
                print("Login Sukses!\n")
                return False
    print("Username atau Password salah. Silakan coba lagi!\n")
    return False

akun = input("Apakah anda sudah mendaftar?")
if (akun == "Y" or akun=="y"):
    print("Silahkan Login")
    login()
elif (akun == "N" or akun== "n"):
    print("Silahkan Mendafatar")
    registrasi()
else :
    print("Input Tidak Valid")


    
       

