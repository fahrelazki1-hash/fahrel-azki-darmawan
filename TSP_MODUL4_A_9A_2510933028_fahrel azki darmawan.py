nama = ["One Ok Rock", "Stray Kids", "Feast", "One Direction (Reborn)", "Kendrick Lamar"]
agency = ["United Talent Agency", "JYP Entertainment", "Rusa Record", "Syco Music", "Wasserman Music"]
asal = ["Jepang", "Korea Selatan", "Indonesia", "Inggris", "USA"]
fee = [150000, 400000, 10000, 1500000, 750000]
hit_song = ["Stand Out Fit In", "Maniac", "Peradaban", "What Make You Beautiful", "Humble"]
durasi = [29, 30, 31, 30, 29]

while True:
    print("""
===== MENU PROGRAM =====
1. Tampilkan Daftar
2. Tambah Data
3. Hapus Data
4. Update Data
5. Total Estimasi Biaya
6. Rata-rata Fee
7. Pendapatan Bersih Artis
8. Keluar
""")

    pilihan = int(input("Pilih menu: "))

    # 1. Tampilkan Data
    if pilihan == 1:
        print("\nDaftar Artis & Band:")
        for i in range(len(nama)):
            print(f"{i+1}. {nama[i]} | {asal[i]} | Fee ${fee[i]} | Durasi {durasi[i]} hari")

    # 2. Tambah Data
    elif pilihan == 2:
        nama.append(input("Masukkan nama artis: "))
        agency.append(input("Masukkan agency: "))
        asal.append(input("Masukkan asal negara: "))
        fee.append(int(input("Masukkan fee: ")))
        hit_song.append(input("Masukkan hit single: "))
        durasi.append(int(input("Masukkan durasi kontrak: ")))
        print("Data berhasil ditambahkan")

    # 3. Hapus Data (request kamu)
    elif pilihan == 3:
        cari = input("Masukkan nama artis yang ingin dihapus: ")

        if cari in nama:
            for artis in nama:  # loop memakai value, bukan index
                if artis == cari:
                    idx = nama.index(artis)

                    nama.remove(artis)
                    agency.remove(agency[idx])
                    asal.remove(asal[idx])
                    fee.remove(fee[idx])
                    hit_song.remove(hit_song[idx])
                    durasi.remove(durasi[idx])

                    print("Data berhasil dihapus!")
                    break
        else:
            print("Data tidak ditemukan")

    # 4. Update Data
    elif pilihan == 4:
        cari = input("Nama artis yang ingin diperbarui: ")

        if cari in nama:
            i = nama.index(cari)
            pilih_upd = int(input("Update (1) Fee / (2) Durasi: "))

            if pilih_upd == 1:
                fee[i] = int(input("Masukkan fee baru: "))
            elif pilih_upd == 2:
                durasi[i] = int(input("Masukkan durasi baru: "))
            else:
                print("Pilihan tidak valid!")
                continue

            print("Data berhasil diperbarui!")
        else:
            print("Data tidak ditemukan!")

    # 5. Total Estimasi Biaya
    elif pilihan == 5:
        cari = input("Masukkan nama artis: ")

        if cari in nama:
            i = nama.index(cari)
            total = fee[i] * durasi[i]
            print(f"\nTotal biaya kontrak {nama[i]} = ${total}")
        else:
            print("Artis tidak ditemukan!")

    # 6. Rata-rata Fee
    elif pilihan == 6:
        print(f"\nRata-rata fee artis = ${sum(fee) / len(fee):.2f}")

    # 7. Pendapatan Bersih
    elif pilihan == 7:
        cari = input("Masukkan nama artis: ")

        if cari in nama:
            i = nama.index(cari)
            biaya = fee[i] * durasi[i]

            if asal[i].lower() == "indonesia":
                pajak = 0.08
            else:
                pajak = 0.18

            bersih = biaya * (1 - pajak)

            print("\nPendapatan Bersih Artis")
            print("----------------------------------")
            print(f"Nama Artis       : {nama[i]}")
            print(f"Asal Negara      : {asal[i]}")
            print(f"Fee x Durasi     : ${fee[i]} x {durasi[i]} hari = ${biaya}")
            print(f"Tarif Pajak      : {int(pajak*100)}%")
            print(f"Pendapatan Bersih: ${bersih}")
            print("----------------------------------\n")
        else:
            print("Nama artis tidak ditemukan!")

    # 8. Keluar
    elif pilihan == 8:
        print("Program selesai.")
        break

    else:
        print("Input tidak valid!")