# program untuk mengevaluasi kinerja siswa berdasarkan persentase 1
# 1
def evaluate_performance(percentage): # mendefinisikan fungsi yang menerima argumen
    if percentage >= 90:
        return "Excellent performance" # if, elif, else = struktur pengkondisian untuk mengevaluasi kinerja berdasarkan nilai persentase
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Needs improvement"  
percentage = float(input("Masukkan persentase siswa: ")) # mengambil input pengguna, diubah ke bentuk angka desimal
print(evaluate_performance(percentage)) # mencetak hasil evaluasi kerja berdasarkan presentase nilai yang dimasukan

# 2
def find_largest(a, b, c): # mendefinisikan fungsi yang menerima 3 angka (a,b,c) sbg argumen
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c: # if elif else = membandingkan ketiga angka tsb untuk menemukan yang terbesar
        return b
    else:
        return c
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: ")) # float = mengambil input dalam bentuk angka desimal
c = float(input("Masukkan angka ketiga: "))
print("Angka terbesar adalah:", find_largest(a, b, c)) # mencetak hasil terbesar

# 3
def fibonacci(n): # menghitung deret fibonacci hingga batas n
    fib_series = [] # mendefinisikan list kosong untuk menyimpan deret fibonacci
    a, b = 0, 1 # mendefinisikan 2 angka pertama dalam deret fibonacci
    while a <= n: # pengulangan untuk menghitung angka dalam deret selama angka Fibonacci lebih kecil atau sama dengan n
        fib_series.append(a) # menambahkan angka fibonacci ke dalam list
        a, b = b, a + b # mengupdate nilai
    return fib_series
n = int(input("Masukkan batas nilai Fibonacci: "))
print("Deret Fibonacci:", fibonacci(n)) # mencetak deret fibonacci yang sudah dihitung

# 4
def print_odd_numbers(n): # mencetak bilangan ganjil
    odd_numbers = [] # list kosong untuk bilangan ganjil
    for i in range(1, n+1, 2): # pengulangan
        odd_numbers.append(i) # menambahkan angka ganjil kedalam list
    return odd_numbers # mengembalikan list yang berisi bilangan ganjil
n = int(input("Masukkan batas nilai: ")) 
print("Bilangan ganjil hingga", n, ":", print_odd_numbers(n)) # mencetak bilangan ganjil yang ada di list

# 5
def print_pattern(n): # mencetak pola berdasarkan nilai
    for i in range(1, n + 1): # pengulangan dari 1 hingga n
        print((str(i) + ' ') * i) # membentuk string 
n = int(input("Masukkan nilai n: "))
print_pattern(n) # mencetak hasil pengulangan