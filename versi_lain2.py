import csv
import os
total_pesanan=[]
total_harga=0
total = 0
kembalian = 0
pembayaran=0

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
            pesanan=[]
            
            nama_menu = data[j-1][1]
            harga = data[j-1][2]
            pesanan.append(nama_menu)
            pesanan.append(int(harga))
            pesanan.append(int(qt))
            print(pesanan)
            total_pesanan.append(pesanan)
            print(total_pesanan)

            tambah = input("Apakah ada tambahan? \n[Y] = Ya | [N] = Tidak : ")
            if tambah == "y":
                pembelian()
            elif tambah == "n":
                print(total_pesanan)
                no_meja = input("Input No Meja\t: ")
                total_pembayaran = 0
                for i in range (0,len(total_pesanan)):
                    total_pembayaran = total_pembayaran + (total_pesanan[i][1]*total_pesanan[i][2])
                print ('Total pembayaran: Rp ',total_pembayaran)
                

            else:
                print("Input salah")
                


        


                
                    


      
    
    
    

        
