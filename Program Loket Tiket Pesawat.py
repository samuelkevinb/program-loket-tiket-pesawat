print("\nSelamat Datang Di Pesawat Penerbangan")
print("============ SAM FLIGHT AIR ============")
print()

# Memilih Maskapai
print("Pilih Maskapai Penerbangan:")
print("1. Air Asia")
print("2. Citilink")
print("3. Garuda Indonesia")

maskapai = input("Masukkan Pilihan Maskapai (1/2/3): ")

if maskapai == "1":
    nama_maskapai = "Air Asia"
    kode_penerbangan = {
        "101": ("ENGLAND", 7000000),
        "102": ("BALI", 3000000),
        "103": ("USA", 8000000),
        "104": ("JAPAN", 5000000),
        "105": ("KOREA", 6000000)
    }
elif maskapai == "2":
    nama_maskapai = "Citilink"
    kode_penerbangan = {
        "201": ("ENGLAND", 4000000),
        "202": ("BALI", 1200000),
        "203": ("USA", 4500000),
        "204": ("JAPAN", 1700000),
        "205": ("KOREA", 2500000)
    }
elif maskapai == "3":
    nama_maskapai = "Garuda Indonesia"
    kode_penerbangan = {
        "301": ("ENGLAND", 10000000),
        "302": ("BALI", 5000000),
        "303": ("USA", 11000000),
        "304": ("JAPAN", 7000000),
        "305": ("KOREA", 8500000)
    }
else:
    print("Pilihan maskapai tidak valid.")
    exit()

print(f"\nAnda memilih maskapai: {nama_maskapai}")
print("\n Kode Penerbangan   |   Tujuan  |   Harga Tiket  ")
print("-------------------------------------------------")
for kode, (tujuan, harga) in kode_penerbangan.items():
    print(f"{kode:<20} | {tujuan:<8} | RP. {harga:,}")
print("-------------------------------------------------")
print("\n")
print("============ FORM DATA SAM FLIGHT AIR ============")
pembeli = str(input("Nama = "))
notelp = int(input("Nomor Telepon = "))
tujuan = input("Kode Tujuan Penerbangan = ")

# Mengecek kode penerbangan dan menentukan harga
if tujuan in kode_penerbangan:
    namatujuan, harga = kode_penerbangan[tujuan]
    print(f"Tujuan Penerbangan = {namatujuan}")
else:
    print("Kode Penerbangan tidak ada")
    exit()

jumlahbeli = int(input("Jumlah Pembelian Tiket = "))

# Menghitung total harga sebelum diskon
total = jumlahbeli * harga

# Cek jika mendapatkan diskon
diskon = 0
if jumlahbeli > 3:
    diskon = 0.1 * total  # Diskon 10%
    print(f"Selamat! Anda mendapatkan diskon 10% karena membeli lebih dari 3 tiket.")
else:
    print("Pembelian kurang dari 3 tiket, tidak mendapatkan diskon.")

# Total setelah diskon
total_setelah_diskon = total - diskon

# Menampilkan detail transaksi
print("=======================================")
print("  MASKAPAI SAM FLIGHT AIR  ")
print("=======================================")
print("Nama Maskapai       : " + str(nama_maskapai))
print("Nama Pembeli        : " + str(pembeli))
print("No. Handphone       : " + str(notelp))
print("Kode Penerbangan    : " + str(tujuan))
print("Tujuan Penerbangan  : " + str(namatujuan))
print("Harga Tiket         : RP. " + "{:,}".format(harga))
print("Jumlah Beli Tiket   : " + str(jumlahbeli))
print("Total Pembayaran    : RP. " + "{:,}".format(total))
if diskon > 0:
    print("Diskon              : RP. " + "{:,}".format(int(diskon)))
    print("Keterangan Diskon   : Anda mendapatkan diskon 10% karena membeli lebih dari 3 tiket.")
print("Total Setelah Diskon: RP. " + "{:,}".format(int(total_setelah_diskon)))
print("=======================================")

# Pembayaran dan kembalian
bayar = int(input("Masukan Uang Pembayaran Anda : "))
kembalian = bayar - total_setelah_diskon
print("Uang Kembalian : RP. " + "{:,}".format(int(kembalian)))
