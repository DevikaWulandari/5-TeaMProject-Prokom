import csv
import os

total_harga=0
total = 0
kembalian = 0
pembayaran=0
pesanan=[]
def menu():
    print("         -WELCOME TO SUNSET RESTORAN-            ")
    print("=================================================")
   

    

    with open('menu.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)



    for x in range(len(data)):
        print(data[x][0],". " ,data[x][1],"= Rp.",data[x][2])
    #mengaktifkan program pembelian
    pembelian()

def pembelian():
    
    j=int(input("Masukkan Pesanan : "))
    qt = int(input('Masukkan Jumlah Pesanan : '))
    with open('menu.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for x in range(len(data)):
        id = int(data[x][0])
        if j == id:
            
            nama_menu = data[j-1][1]
            harga = data[j-1][2]
            pesanan.append({"nama" : nama_menu, "kuantitas" : qt, "harga" : harga})

            
            while True:
                tambah = input("Apakah ada tambahan? \n[Y] = Ya | [N] = Tidak : ")
                if tambah == "y":
                    pembelian()
                    break
                elif tambah == "n":
                    no_meja = input("Input No Meja\t: ")
                    total_pembayaran = 0
                    keys = pesanan[0].keys()
                    with open('pesanan.csv', 'a', newline='')  as output_file:
                        dict_writer = csv.DictWriter(output_file, keys)
                        dict_writer.writerows(pesanan)
                    pembayarann()
                    break
                else:
                    print("Input salah")
  
def pembayarann():
    i=0
    global total
    global pembayaran
    global kembalian
    global total_harga
    print("=============================================================")
    print("     Nama Menu      |    Harga    | Kuantitas |    Total    |")
    print("=============================================================")
    
    for dictionary in pesanan: 
            total_harga += int(dictionary["kuantitas"])*float(dictionary["harga"])

    for dictionary in pesanan:
        print ("    {}\t         {}\t        {}\t  {}".format(dictionary['nama'],dictionary['harga'],dictionary['kuantitas'], int(dictionary['kuantitas'])
                                                                  *float(dictionary['harga'])))

    print("=============================================================\n")
    total = total_harga
    print("Total Pembayaran : %d" %total)
    pembayaran = float(input("CASH\t\t : "))
    kembalian = pembayaran-total
    print("Kembalian\t : %d" %kembalian)