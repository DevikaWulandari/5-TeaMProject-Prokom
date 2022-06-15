import csv
from versi_lain2 import *

def registrasi():
    with open('username.csv', 'a') as f:
        writer = csv.writer(f)
        user = input("Username : ")
        pw = input("Password : ")
        writer.writerow([user,pw])
    with open('username.csv', 'a') as f:
        pass
    print("\nSilahkan Login")
    return 'success'

def login():

    with open("username.csv", "r") as x:
        user = input("Username : ")
        pw = input("Password : ")
        reader = csv.reader(x, delimiter=",")
        for row in reader:
            if row == ([user,pw]):
                print("Login Sukses!\n")
                menu()
                return False
    print("Username atau Password salah. Silakan coba lagi!\n")
    login()
    return False