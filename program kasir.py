import csv

list_menu=[]
total_harga=0
total = 0
kembalian = 0
pembayaran=0

def menu():
    print("         -WELCOME TO SUNSET RESTORAN-            ")
    print("=================================================")
    print(" Kode Menu |      Nama Menu     |     Harga     |")
    print("=================================================")
    print("     1.          Nasi Goreng         Rp.14000    ")
    print("     2.          Mie Ayam            Rp.13000    ")
    print("     3.          Ayam Goreng         Rp.20000    ")
    print("     4.          Ayam Bakar          Rp.20000    ")
    print("     5.          Lele Goreng         Rp.12000    ")
    print("     6.          Jus Mangga          Rp.10000    ")
    print("     7.          Es teh               Rp.4000    ")
    print("     8.          Es Jeruk             Rp.5000    ")
    print("     9.          Teh Panas            Rp.4000    ")
    print("    10.          Air putih            Rp.2000    ")
    print("=================================================\n")
    #mengaktifkan program pembelian
    pembelian()

def pembelian():
    i=0
    no_meja = int(input("Masukkan No Meja : "))
    jumlah_beli = int(input("Masukkan Jumlah Pembelian : "))
    for x in range(jumlah_beli): 
        print("Data Menu Ke - ", i+1)
        kode_menu= int(input("Kode Menu : "))
        if kode_menu == 1:
            nama_menu = "Nasi Goreng"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 14000
        elif kode_menu == 2:
            nama_menu = "Mie Ayam"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 13000
        elif kode_menu == 3:
            nama_menu = "Ayam Goreng"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 20000
        elif kode_menu == 4:
            nama_menu = "Ayam Bakar"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 20000
        elif kode_menu == 5:
            nama_menu = "Lele Goreng"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 12000
        elif kode_menu == 6:
            nama_menu = "Jus Mangga"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = (kuantitas*10000)
        elif kode_menu == 7:
            nama_menu = "Es Teh"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 4000
        elif kode_menu == 8:
            nama_menu = "Es Jeruk"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 5000
        elif kode_menu == 9:
            nama_menu = "Teh Panas"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 4000
        elif kode_menu == 10:
            nama_menu = "Air Putih"
            print("Nama Menu :", nama_menu)
            kuantitas= int(input("Kuantitas : "))
            harga = 2000
        else:
            print("Kode Salah")
            break
        i=i+1
        list_menu.append({"nama" : nama_menu, "kuantitas" : kuantitas, "harga" : harga})
           
    #menambahkan lagi
    input("Tekan 'ENTER' untuk Melanjutkan")
    kondisi = input("Ingin pesan lagi? (Y/T) : ")
    if kondisi == "y" or kondisi == "Y":
        pembelian()
    elif kondisi == "t" or kondisi == "T":
        pembayaran()
        
    #Mencatat Transaksi di CSV 'pesanan'
    keys = list_menu[0].keys()
    with open('pesanan.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_menu)
        
def pembayaran():
    i=0
    global total
    global pembayaran
    global kembalian
    global total_harga
    print("=============================================================")
    print("     Nama Menu      |    Harga    | Kuantitas |    Total    |")
    print("=============================================================")
    
    for dictionary in list_menu: 
            total_harga += int(dictionary["kuantitas"])*float(dictionary["harga"])

    for dictionary in list_menu:
        print ("    {}\t         {}\t        {}\t  {}".format(dictionary['nama'],dictionary['harga'],dictionary['kuantitas'], int(dictionary['kuantitas'])
                                                                  *float(dictionary['harga'])))

    print("=============================================================\n")
    total = total_harga
    print("Total Pembayaran : %d" %total)
    pembayaran = float(input("CASH\t\t : "))
    kembalian = pembayaran-total
    print("Kembalian\t : %d" %kembalian)



#Mengaktifkan Program
awal = True
if awal == True:
    menu()
                