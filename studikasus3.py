daftar_buku = ("hyouka", "fadil bayangan", "tutorial makan dan minum", "malaikat subuh", "cara dapat 1 triliun tanpa bekerja", "86", "cara masak ala fery")
pinjaman = []

print("=== PERPUSTAKAAN FAKULTAS TEKNIK ===")
nama = input("masukkan nama anda: ")
print("halo", nama)
print("\nDaftar Buku:")

for buku in daftar_buku:
    print("-", buku)

while True:
    pilihan = input("\nMasukkan judul buku yang ingin dipinjam (ketik 'selesai' untuk berhenti): ")

    if pilihan.lower() == "selesai":
        break

    if pilihan in daftar_buku:
        pinjaman.append(pilihan)
        print("Buku berhasil dipinjam.")
    else:
        print("Buku tidak tersedia.")

print("\n=== DAFTAR PINJAMAN ===")

if len(pinjaman) == 0:
    print("Belum ada buku yang dipinjam.")
else:
    for buku in pinjaman:
        print("-", buku)

while len(pinjaman) > 0:
    hapus = input("\nApakah ingin menghapus buku dari pinjaman? (ya/tidak): ")

    if hapus.lower() == "tidak":
        break

    if hapus.lower() == "ya":
        buku_hapus = input("Masukkan judul buku yang ingin dihapus: ")

        if buku_hapus in pinjaman:
            pinjaman.remove(buku_hapus)
            print("Buku berhasil dihapus.")
        else:
            print("Buku tersebut tidak ada dalam daftar pinjaman.")
    else:
        print("Pilihan tidak valid.")

print("\n=== BUKU YANG DIPINJAM ===")

if len(pinjaman) == 0:
    print("Tidak ada buku yang dipinjam.")
else:
    for buku in pinjaman:
        print("-", buku)

