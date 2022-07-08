besar_ruangan = float(input("Masukkan besar ruangan : "))
jumlah_orang = float(input("Masukkan jumlah orang : "))
suhu_cuaca_luar = float(input("Masukkan suhu cuaca luar : "))

# nilai xmax
x_max_br = 50
x_max_jo = 15
x_max_cl = 32
x_max_sa = 26

# nilai xmin
x_min_br = 20
x_min_jo = 5
x_min_cl = 22
x_min_sa = 18

# true  = Luas
# false = sempit
keterangan_br = bool

# true =  banyak
# false = sedikit
keterangan_jo = bool

# true = cerah-panas
# false = hujan-dingin
keterangan_cl = bool

# true = naikan-suhu
# false = turun-suhu
keterangan_sa = bool


def cekBesarRuangan(cek_besar_ruangan):
    if 20 <= cek_besar_ruangan <= 34:
        keterangan_br = False
        # print(keterangan_br)
    elif cek_besar_ruangan >= 35 and cek_besar_ruangan <= 50:
        keterangan_br = True
        # print(keterangan_br)
    return keterangan_br


def cekJumlahOrang(cek_jumlah_orang):
    if 5 <= cek_jumlah_orang <= 9:
        keterangan_jo = False
        # print(keterangan_jo)
    elif cek_jumlah_orang >= 10 and cek_jumlah_orang <= 15:
        keterangan_jo = True
        # print(keterangan_jo)
    return keterangan_jo


def cekSuhuCuacaLuar(cek_suhu_cuaca_luar):
    if 22 <= cek_suhu_cuaca_luar <= 26:
        keterangan_cl = False
        # print(keterangan_cl)
    elif cek_suhu_cuaca_luar >= 27 and cek_suhu_cuaca_luar <= 32:
        keterangan_cl = True
        # print(keterangan_cl)
    return keterangan_cl

def cekSuhuAc(cek_suhu_ac):
    if 18 <= cek_suhu_ac <= 21:
        keterangan_sa = False
        print(keterangan_sa)
    elif cek_suhu_ac >= 22 and cek_suhu_ac <= 26:
        keterangan_sa = True
        print(keterangan_sa)
    

# cekBesarRuangan(25)
cek_br = cekBesarRuangan(besar_ruangan)
cek_jo = cekJumlahOrang(jumlah_orang)
cek_cl = cekSuhuCuacaLuar(suhu_cuaca_luar)

# kekiri


def keKiri(xmax, xmin, x):
    hasil_ke_kiri = (xmax - x) / (xmax - xmin)
    return hasil_ke_kiri


def keKanan(xmax, xmin, x):
    hasil_ke_kanan = (x-xmin) / (xmax-xmin)
    return hasil_ke_kanan


kiri_br = keKiri(x_max_br, x_min_br, besar_ruangan)
kanan_br = keKanan(x_max_br, x_min_br, besar_ruangan)

kiri_jo = keKiri(x_max_jo, x_min_jo, jumlah_orang)
kanan_jo = keKanan(x_max_jo, x_min_jo, jumlah_orang)

kiri_cl = keKiri(x_max_cl, x_min_cl, suhu_cuaca_luar)
kanan_cl = keKanan(x_max_cl, x_min_cl, suhu_cuaca_luar)


# def cek(keterangan_br , keterangan_jo , keterangan_cl  )
# print(cek_br)
# print(cek_jo)
# print(cek_cl)

if cek_br == False and cek_jo == False and cek_cl == False:
    alfa = min(kiri_br, kiri_jo, kiri_cl)
    suhu_ac = 18 + (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == False and cek_jo == False and cek_cl == True:
    alfa = min(kiri_br, kiri_jo, kanan_cl)
    suhu_ac = 26 - (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == False and cek_jo == True and cek_cl == False:
    alfa = min(kiri_br, kanan_jo, kiri_cl)
    suhu_ac = 26 - (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == False and cek_jo == True and cek_cl == True:
    alfa = min(kiri_br, kanan_jo, kanan_cl)
    suhu_ac = 26 - (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == True and cek_jo == False and cek_cl == False:
    alfa = min(kanan_br, kiri_jo, kiri_cl)
    suhu_ac = 18 + (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == True and cek_jo == False and cek_cl == True:
    alfa = min(kanan_br, kiri_jo, kanan_cl)
    suhu_ac = 18 + (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == True and cek_jo == True and cek_cl == False:
    alfa = min(kanan_br, kanan_jo, kiri_cl)
    suhu_ac = 26 - (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)
elif cek_br == True and cek_jo == True and cek_cl == True:
    alfa = min(kanan_br, kanan_jo, kiri_cl)
    suhu_ac = 26 - (alfa*(26-18))
    print(suhu_ac)
    cekSuhuAc(suhu_ac)