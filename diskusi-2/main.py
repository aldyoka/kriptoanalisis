import os.path
import re
from collections import Counter

dokumen_name = ''
doc = ''


def cek_doc():
    if os.path.exists(dokumen_name):
        global doc
        doc = open(dokumen_name, 'r+')
        proses()
    else:
        print('dokumen Yang Anda inginkan tidak tersedia')
        exit()


def proses():
    # membaca semua line yang ada
    kata = (' '.join(line.strip() for line in doc))

    # merubah semua huruf kapital menjadi huruf kecil
    new_kata = kata.lower()

    # proses menghilangkan simbol dan spasi
    ubah = re.compile("[^a-zA-Z]")
    new_kata = ubah.sub('', new_kata)
    total = 0
    for _ in new_kata:
        total += 1

    # menentukan banyaknya char yang dianalisis
    car = int(1)
    # menentukan frekuensi
    array = [(new_kata[i:i + car]) for i in range(0, len(new_kata), car)]
    frekuensi = Counter(array)

    for i in sorted(frekuensi):
        print(' ' + i + '\n| Karakter Yang Sama: ' + str(frekuensi[i]) + ',\n| Peluang : ' +
              str(int(frekuensi[i])/total*100) + '%')
    print('Jumlah Silabel atau Total Karakter Keseluruhan: ' + str(total))


def main():
    global dokumen_name
    dokumen_name = input('Masukkan Nama Dokumen Yang Akan Dianalisis: ')
    dokumen_name = dokumen_name + '.txt'
    cek_doc()


main()
