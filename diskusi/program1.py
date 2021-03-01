
def bilangan_prima():
    print("\nBilangan Prima")
    if bilangan > 1:
        for i in range(2, bilangan):
            if (bilangan % i) == 0:
                print(bilangan, "bukan bilangan prima")
                break
        else:
            print(bilangan,"adalah bilangan prima")
    else:
        print(bilangan, "bukan bilangan prima")

def fpb():
    print("\nFPB")
    def hitung(bil1, bil2):
        if (bil2 == 0):
            return bil1
        else:
            return hitung(bil2, bil1 % bil2)

    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
    bil = hitung(bil1, bil2)
    print("Faktor persekutuan terbesarnya adalah ", bil)

def fac():
    print("\nFakorial")
    def faktorial(bilangan):
        if bilangan == 1:
            return bilangan
        else:
            return bilangan * faktorial(bilangan - 1)

    if bilangan < 0:
        print("Bilangan faktorial yang cari tidak boleh bilangan negatif")
    elif bilangan == 0:
        print("Faktorial dari 0 adalah 1")
    else:
        print("Faktorial dari", bilangan, "adalah", faktorial(bilangan))

def input_bil():
    global bilangan
    bilangan = int(input("Masukkan bilangan yang ingin anda cek: "))


loop = "y"
while loop == "y":
    input_bil()
    bilangan_prima()
    fac()
    fpb()
    loop = input("apakah anda ingin mengulang ?(y/n): ")