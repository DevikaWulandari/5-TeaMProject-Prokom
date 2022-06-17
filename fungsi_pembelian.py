import csv

total_harga=0
total = 0
kembalian = 0
pembayaran=0
pesanan=[]

#bagian pemesanan
def pembelian():
    global pesanan    
    while True:
        j=input("Masukkan Kode Pesanan : ")
        qt = input('Masukkan Jumlah Pesanan : ')

        if j.isnumeric() and qt.isnumeric():
            j=int(j)
            qt=int(qt)
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
                        if (tambah == "Y" or tambah =="y"):
                            pembelian()
                            break
                        elif (tambah == "N"or tambah =="n"):
                            no_meja = input("Input No Meja\t: ")
                            total_pembayaran = 0
                            #mencetak pesanan ke csv
                            keys = pesanan[0].keys()
                            with open('pesanan.csv', 'a', newline='')  as output_file:
                                dict_writer = csv.DictWriter(output_file, keys)
                                dict_writer.writerows(pesanan)
                            pembayarann()
                            
                            exit()
                        else:
                            print("Input Anda salah")
        else:
            print("Input Anda Salah")
            pembelian()
            break
        
#mencetak struk pembelian
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
            total_harga += int(dictionary["kuantitas"])*float(dictionary["harga"]) #menghitung total harga

    for dictionary in pesanan: #mencetak pembelian yang telah dipilih
        print ("    {}\t         {}\t        {}\t  {}".format(dictionary['nama'],dictionary['harga'],dictionary['kuantitas'], int(dictionary['kuantitas'])
                                                                  *float(dictionary['harga']))) 

    print("=============================================================\n")
    total = total_harga
    print("Total Pembayaran : %d" %total)
    pembayaran = float(input("CASH\t\t : ")) #input uang yang harus dibayarkan
    kembalian = pembayaran-total
    print("Kembalian\t : %d" %kembalian)                    