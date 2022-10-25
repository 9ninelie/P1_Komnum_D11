"""
Pastikan telah melakukan instalasi matplotlib dan tabulate melalui pip (dengan menggunakan cmd)
sintaks instalasi:

pip install matplotlib
pip install tabulate

"""

"""
Kelompok 11 Komnum D:

-   Danno Denis Dhaifullah	        5025211027
-   Arif Nugraha Santosa	        5025211048
-   Laurivasya Gadhing Syahafidh	5025211136

"""

import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


#inisiasi variabel
#ini value xnya
x1 = []
x2 = []
x3 = [] 
#ini value dari f(xi)
y1 = []
y2 = []
y3 = []  

print("\n- - - - - Metode Bolzano - - - - -\n")

iterasi = int(input("Banyak iterasi\t: "))
print("Nilai x yang dicari terletak diantara")
lowx = float(input("nilai x1: "))
highx = float(input("hingga x2: "))
pangkat_besar = int(input("Masukan pangkat tertinggi dalam persamaan : "))

if(lowx > highx):
    swap = lowx
    lowx = highx
    highx = swap

koefisien = []
i = pangkat_besar
iterasi2 = iterasi

#input koefisien dari bentuk persamaan
while i >= 0 :
    koefisien.append(int(input(f"Masukan nilai koefisien dari x^{pangkat_besar - i} : ")))
    i -= 1

#x4 memiliki nilai angka diantara lowx hingga highx hingga maximal 100 data
x4 = np.linspace(lowx, highx, 100)
y4 = []

k = 0
while k != 100:

    res = 0
    i = pangkat_besar

    while i >= 0 :
        temp = abs(math.pow(x4[k], i)) * int(koefisien[i])
        res += temp
        i -= 1

    y4.append(res)
    k += 1

plt.plot(x4, y4, color = 'black') #menggambar garis
plt.xlabel('x') 
plt.ylabel('y')

temp = 0

#perhitungan x1, x2, x3, fx(x1), fx(x2), fx(x3)
while iterasi > 0 :

    #f(x1)
    res = 0
    i = pangkat_besar   
    while i >= 0 :
        temp = abs(math.pow(lowx, i)) * int(koefisien[i])
        res += temp
        i -= 1
    y1_temp = res

    #f(x2)
    res = 0
    i = pangkat_besar  
    while i >= 0 :
        temp = abs(math.pow(highx, i)) * int(koefisien[i])
        res += temp
        i -= 1
    y2_temp = res

    #f(x3)
    x3_temp = (lowx + highx) / 2
    res = 0
    i = pangkat_besar
    while i >= 0 :
        temp = abs(math.pow(x3_temp, i)) * int(koefisien[i])
        res += temp
        i -= 1
    y3_temp = res
    
    x1.append(lowx)
    x2.append(highx)
    x3.append(x3_temp)
    y1.append(y1_temp)
    y2.append(y2_temp)
    y3.append(y3_temp)

    #swapping variabel x1 atau x2 apabila ada perubahan tanda
    if(y3_temp < 0): lowx = x3_temp
    elif(y3_temp > 0): highx = x3_temp
    
    iterasi -= 1

BanyakIterasi=[]
j = 1
while j <= iterasi2:
    BanyakIterasi.append(j)
    j += 1

tabel = {
    'Iterasi' : BanyakIterasi,
    'x1' : x1,
    'x2' : x2,
    'x3' : x3,
    'f(x1)' : y1,
    'f(x2)' : y2,
    'f(x3)' : y3
}

print(tabulate(tabel, headers = "keys", tablefmt = "double_grid"))

print("Berdasarkan tabel di atas, dapat disimpulkan bahwa persamaan")

while pangkat_besar >= 0: 
    print(f"{koefisien[pangkat_besar]}x^{pangkat_besar}", end = " ")
    if(pangkat_besar != 0 and koefisien[pangkat_besar - 1] > 0): print("+", end = " ")
    pangkat_besar -= 1

print(f"= 0\nMemiliki akar penyelesaian: {x3[iterasi2 - 1]}")

plt.title(label = "Grafik Fungsi Metode Bolzano", color = "black") #judul grafik
plt.grid()

#titik titik tiap x dan y setelah diambil nilai tengahnya
plt.scatter(x3, y3, color = 'cyan')
#titik paling akurat
plt.scatter(x3[iterasi2 - 1], y3[iterasi2 - 1], color = 'red')
plt.show()

# https://pypi.org/project/tabulate/
# https://pypi.org/project/matplotlib/