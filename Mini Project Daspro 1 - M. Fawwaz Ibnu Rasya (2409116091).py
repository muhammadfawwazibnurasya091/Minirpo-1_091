while True:
    JamKerja = float(input("Jam kerja: "))
    TarifKerja = float(input("Tarif kerja: Rp. ")) #inputnya

    TotalGaji = JamKerja * TarifKerja #ngitung total gaji

    if JamKerja > 160:
        TotalGaji *= 1.1
    print("Total gaji: Rp.", TotalGaji)

    pilihan = input("Lagi? (y/n): ") #perulangannya
    if pilihan.lower() != "y":
        break

   