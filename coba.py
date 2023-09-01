for i in range(1, 3 + 1, 1):
    if i == 1:
        print("Masukkan Nilai Quiz")
        a = int(input())
    else:
        if i == 2:
            print("Masukkan Nilai UTS")
            b = int(input())
        else:
            print("Masukkan Nilai UAS")
            c = int(input())
hasil = float(a + b + c) / 3
if hasil >= 80:
    print("Nilai Akhir Kamu " + str(hasil) + " dengan Predikat A")
else:
    if hasil >= 70:
        print("Nilai Akhir Kamu" + str(hasil) + "dengan Predikat B")
    else:
        print("Nilai Akhir Kamu" + str(hasil) + "dengan Predikat C")















print("PRAKTIKUM ALGORITMA PEMROGRAMAN")
input("Nama        : ")
input("NIM         : ")
input("Angkatan    : ")
input("Jurusan     : ")
input("Fakultas    : ")
input("Universitas : ")
print("Nama saya ", nama, "NIM : ", nim ,"Prodi : ", prodi)

p = {1:34}
del p
print (p)