import os.path
import re
from collections import Counter

dokumen_name = ""
doc = ""
frekuensi = ""
total = int


def cek_doc():
    if os.path.exists(dokumen_name):
        global doc
        doc = open(dokumen_name, "r+")
        most_char()
    elif dokumen_name == ".txt":
        print("anda belum memasukan nama file !")
        main()
    else:
        print("dokumen Yang Anda inginkan tidak tersedia")
        exit()


def most_char():
    # membaca semua line yang ada
    kata = (" ".join(line.strip() for line in doc))

    # merubah semua huruf kapital menjadi huruf kecil
    new_kata = kata.lower()

    # proses menghilangkan simbol dan spasi
    ubah = re.compile("[^a-zA-Z]")
    new_kata = ubah.sub("", new_kata)

    # penghitungan character
    global total, frekuensi
    total = 0
    for x in range(len(new_kata)):
        total = int(x) + 1

    # menentukan banyaknya char yang dianalisis
    car = int(1)
    # menentukan frekuensi
    array = [(new_kata[i:i + car]) for i in range(0, len(new_kata), car)]
    frekuensi = Counter(array)

    for i in sorted(frekuensi):
        peluang = float(int(frekuensi[i]) / total * 100)
        print(i + "\n| Karakter Yang Sama: " + str(frekuensi[i]) + ",\n| Peluang : %.2f " % peluang
              + "%")
    print("Jumlah Silabel atau Total Karakter Keseluruhan: " + str(total))


def ganti_karakter():
    if os.path.exists(dokumen_name):
        with open(dokumen_name) as dokumen:
            find_char = input("\nKarakter Yang Diganti : ")
            if find_char in dokumen.read():
                replace_with = input("\nKarakter penganti: ")
                with open(dokumen_name, "r+") as karakter:
                    file = karakter.read()
                    file = file.translate(str.maketrans({find_char: replace_with, replace_with: find_char}))
                    karakter.seek(0)
                    karakter.write(file)
                    karakter.truncate()
            else:
                print("\nEROR! Karakter Yang Akan Dicari Tidak Ada!")
                ganti_karakter()


def main():
    global dokumen_name
    dokumen_name = input("Masukkan Nama Dokumen Yang Akan Dianalisis: ")
    dokumen_name = dokumen_name + ".txt"
    cek_doc()


main()
ganti_karakter()
