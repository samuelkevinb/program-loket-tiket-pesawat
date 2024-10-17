print ("\nSelamat Datang Di Pesawat Penerbangan")
print ("============SAM FLIGHT AIR============")
print()
print (" Kode Penerbangan   |   Tujuan  |   Harga Tiket  ")
print ("-------------------------------------------------")
print ("101                 |   ENG     |   RP. 5.000.000")
print ("102                 |   BALI    |   RP. 1.500.000")
print ("103                 |   USA     |   RP. 5.500.000")
print ("104                 |   JPN     |   RP. 2.000.000")
print ("105                 |   KOR     |   RP. 3.000.000")
print ("-------------------------------------------------")
print ("\n")
print ("============ FORM DATA SAM FLIGHT AIR ============")
pembeli = str(input("Nama = "))
notelp = int(input("Nomor Telepon = "))
tujuan = input("Kode Tujuan Penerbangan = ")

if tujuan == "101":
    print("Tujuan Penerbangan = ENGLAND")
    namatujuan = "ENGLAND"
    harga = 5000000
    
elif tujuan == "102":
    print ("Tujuan Penerbangan = BALI")
    namatujuan = "BALI"
    harga = 1500000

elif tujuan == "103":
    print ("Tujuan Penerbangan = UNITED STATE AMERICA")
    namatujuan = "UNITED STATE AMERICA"
    harga = 5500000

elif tujuan == "104":
    print ("Tujuan Penerbangan = JAPAN")
    namatujuan = "JAPAN"
    harga = 2000000

elif tujuan == "105":
    print ("Tujuan Penerbangan = KOREA")
    namatujuan = "KOREA"
    harga = 3000000

else :
    print ("Kode Penerbangan tidak ada")
    

jumlahbeli = int(input("Jumlah Pembelian Tiket = "))

total = int(jumlahbeli * harga)

print("=======================================")
print("  MASKAPAI SAM FLIGHT AIR  ")
print("=======================================")
print("Nama Pembeli         : " +str(pembeli))
print("No. Handphone        : " +str(notelp))
print("Kode Penerbangan     : " +str(tujuan))
print("Tujuan Penerbangan   : " +str(namatujuan))
print("Harga Tiket          : " +str(harga))
print("Jumlah Beli Tiket    : " +str(jumlahbeli))
print("Total Pembayaran     : " +str(total))
print("=======================================")

bayar = int(input("Masukan Uang Pembayaran Anda : "))
kembalian = int(bayar - total)
print("Uang Kembalian : " +str(kembalian))