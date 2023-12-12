import math


def persegi(sisi):
    luas = sisi ** 2
    keliling = 4 * sisi
    print("Luas Persegi: ", luas)
    print("Keliling Persegi: keliling", keliling)


def persegipanjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang:", luas)
    print("Keliling Persegi Panjang:", keliling)


def segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = alas + alas + alas
    print("Luas Segitiga:", luas)
    print("Keliling Segitiga:", keliling)


def lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari
    print("Luas Lingkaran:", luas)
    print("Keliling Lingkaran:", keliling)


def trapesium(alas_atas, alas_bawah, tinggi):
    luas = 0.5 * (alas_atas + alas_bawah) * tinggi
    keliling = alas_atas + alas_bawah + alas_atas + alas_bawah
    print("Luas Trapesium:", luas)
    print("Keliling Trapesium:", keliling)


def jajargenjang(alas, tinggi):
    luas = alas * tinggi
    keliling = 2 * (alas + alas)
    print("Luas JajarGenjang:", luas)
    print("Keliling JajarGenjang:", keliling)


def belahketupat(d1, d2):
    luas = 0.5 * d1 * d2
    keliling = 4 * d1
    print("Luas belah ketupat:", luas)
    print("Keliling belah ketupat:", keliling)