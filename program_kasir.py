import csv
import os
from fungsi_pembelian import *

#mencetak daftar menu dari csv
def menu():
    print("="*61)
    print('{:^65}'.format("         -WELCOME TO SUNSET RESTORAN-            "))
    print("="*61)
   

    

    with open('menu.csv', newline='') as f: #membuka csv
        reader = csv.reader(f)
        data = list(reader)



    for x in range(len(data)): #mencetak data dari csv
        print(data[x][0],". " ,data[x][1],"= Rp.",data[x][2])


    #mengaktifkan program pembelian
    pembelian()


  

