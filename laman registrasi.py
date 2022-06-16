from auth import *
import csv

def auth():
    print("="*61)
    print('{:^61}'.format('Welcome'))
    print("="*61)
    print()
    akun = 'i'
    while (akun != 'q' or akun!= 'Q'):
        akun = input("Apakah anda sudah mendaftar? \n[Y] = Ya | [N] = Tidak : ")
        if (akun == "Y" or akun=="y"):
            print("Silahkan Login")
            while True:
                state = login()
                if state == False:
                    break
            return False
        elif (akun == "N" or akun== "n"):
            print("Silahkan Mendafatar")
            state = registrasi()
            if state == 'success':
                state1 = True
                while state1 == True:
                    state1 = login()
                    if state1 == False: 
                        break
            return False
        elif (akun =='Q' or akun == 'q'):
            break
        else :
            print("Input Tidak Valid")
        
    


def main():
    auth()
    
main()