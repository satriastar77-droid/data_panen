print("Nama: Julius Satria Agung")
print("NRP: 152024049")
print()
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

for i in data_panen:
    for j in data_panen[i]:
        if j == "nama_lokasi":
            print(f"Nama lokasi: {data_panen[i][j]}")
        if j == "hasil_panen":
            print(f"Padi: {data_panen[i][j]['padi']}")
            print(f"Jagung: {data_panen[i][j]['jagung']}")
            print(f"Kedelai: {data_panen[i][j]['kedelai']}")

print()
print()

print(data_panen['lokasi2']['hasil_panen']['jagung'])

print()
print()

print(data_panen['lokasi3']['nama_lokasi'])

print()

jumlah_padi = []
jummlah_kedelai = []
for i in data_panen:
    for j in data_panen[i]:
        if j == "hasil_panen":
            jumlah_padi.append(data_panen[i][j]['padi'])
            jummlah_kedelai.append(data_panen[i][j]['kedelai'])
            
total_padi = sum(jumlah_padi)
print(f"Jumlah padi: {total_padi}") 

total_kedelai = sum(jummlah_kedelai)
print(f"Jumlah kedelai: {total_kedelai}")

print()

for i in data_panen:
    print(i)
    for j in data_panen[i]:
        if j == "hasil_panen":
            print(f"Jumlah padi: {data_panen[i][j]['padi']}")
            print(f"Jumlah jagung: {data_panen[i][j]['jagung']}")
            if data_panen[i][j]['padi'] > 1300 or data_panen[i][j]['jagung'] > 800:
                print("Memerlukan perhatian khusus")
            else:
                print("Kondisi Baik")