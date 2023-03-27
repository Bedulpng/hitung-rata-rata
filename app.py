# Memenita pengguna untuk memasukan nilai numeria
input_str = input("Masukan nilai-nilai numerik, pisahkan dengan koma: ")

# Memisahkan nilai-nilai numerik menjadi list
nilai_list = input_str.split(",")

# Mengubah nilai dalam list dari string ke float
nilai_list = [float(nilai) for nilai in nilai_list]

# Menghitung rata_rata dari nilai dalam list
rata_rata = sum(nilai_list) / len(nilai_list)

# Mencetak hasil
print("nilai rata-ratanya adalah:", rata_rata)