import csv
import os
from fungsi_pembelian import *


def menu():
    print("="*61)
    print('{:^65}'.format("         -WELCOME TO SUNSET RESTORAN-            "))
    print("="*61)
   

    

    with open('menu.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)



    for x in range(len(data)):
        print(data[x][0],". " ,data[x][1],"= Rp.",data[x][2])


    #mengaktifkan program pembelian
    pembelian()
   


  

