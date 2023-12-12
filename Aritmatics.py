import math
def tambah(bil1, bil2): 
    hasil = bil1 + bil2
    print("Hasil tambah dari", bil1, "+", bil2, "=", hasil)


def kurang(bil1, bil2): 
    hasil = bil1 - bil2
    print("Hasil pengurangan dari", bil1, "-", bil2, "=", hasil)


def kali(bil1, bil2): 
    hasil = bil1 * bil2
    print("Hasil perkalian dari", bil1, "*", bil2, "=", hasil)


def bagi(bil1, bil2): 
    hasil = bil1 / bil2
    print("Hasil pembagian dari", bil1, "/", bil2, "=", hasil)


def pangkat(bil1, bil2): 
    hasil = math.pow (bil1, bil2)
    print("Hasil pangkat dari", bil1, "^", bil2, "=", hasil)


def modulus (bil1, bil2 ) :
    hasil = bil1 % bil2
    print ("Hasil modulus dari", bil1, "&", bil2, "=", hasil)

def akar (bil1, bil2 ) :
    bil2 = 0.5
    hasil = bil1 ** bil2
    print ("Hasil akar dari", bil1, "=", hasil)

def pembulatan (bil1) :
    hasil = math.ceil(bil1)
    print ("Hasil bulatkan keatas dari", bil1, "=", hasil)

def logaritma_dasar10(bil1):
    hasil = math.log10(bil1)
    print(f"Hasil Logaritma dasar 10 dari {bil1} = {hasil}")

def akar_kompleks(bil1):
    hasil = math.sqrt(bil1)
    print(f"Hasil akar kompleks dari {bil1} = {hasil}")

