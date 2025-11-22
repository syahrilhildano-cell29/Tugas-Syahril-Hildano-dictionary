print ("Nama: syahril hildano")
print ("kelas: Ti 25 c5")
print ("Nim: 312510295")


# Program Daftar Nilai Mahasiswa (Dictionary)

mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return tugas * 0.30 + uts * 0.35 + uas * 0.35

while True:
    print("\n=== MENU PILIHAN ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    # Tambah Data
    if pilihan == "1":
        nama = input("Nama Mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        akhir = hitung_nilai_akhir(tugas, uts, uas)

        mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil ditambahkan!")

    # Ubah Data
    elif pilihan == "2":
        nama = input("Nama yang akan diubah: ")
        if nama in mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            akhir = hitung_nilai_akhir(tugas, uts, uas)

            mahasiswa[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    # Hapus Data
    elif pilihan == "3":
        nama = input("Nama yang akan dihapus: ")
        if nama in mahasiswa:
            del mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    # Tampilkan Semua Data
    elif pilihan == "4":
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        if mahasiswa:
            for nama, data in mahasiswa.items():
                print(f"{nama} | Tugas: {data['tugas']} | UTS: {data['uts']} | UAS: {data['uas']} | Akhir: {data['akhir']:.2f}")
        else:
            print("Belum ada data!")

    # Cari Data
    elif pilihan == "5":
        nama = input("Nama yang dicari: ")
        if nama in mahasiswa:
            d = mahasiswa[nama]
            print(f"{nama} | Tugas: {d['tugas']} | UTS: {d['uts']} | UAS: {d['uas']} | Akhir: {d['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # Keluar
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
