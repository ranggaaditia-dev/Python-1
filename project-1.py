print ("\nMENJUAL ALAT ALAT BELAJAR")

BUKU = 25000
while BUKU:
    BUKU = int(input("\nMasukan harga anda :"))
    if BUKU == 25000:
        print("SALDO ANDA CUKUP BELI BUKU")
    elif BUKU >= 15000:
        print("SALDO ANDA HANYA CUKUP BELI PULPEN")
    else:
        print("SALDO ANDA TIDAK CUKUP")