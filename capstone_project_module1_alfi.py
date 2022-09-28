listMobil = [
    {
        'mobil' : 'TOYOTA AVANZA',
        'unit' : 10,
        'tahun' : 2018,
        'kapasitas' : 6,
        'harga' : 350000,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    },
    {
        'mobil' : 'HONDA BRIO',
        'unit' : 7,
        'tahun' : 2017,
        'kapasitas' : 5,
        'harga' : 450000
    },
    {
        'mobil' : 'WULING CORTEZ',
        'unit' : 4,
        'tahun' : 2019,
        'kapasitas' : 7,
        'harga' : 650000
    },
    {
        'mobil' : 'INNOVA REBORN',
        'unit' : 5,
        'tahun' : 2018,
        'kapasitas' : 7,
        'harga' : 950000
    },
    {
        'mobil' : 'FORTUNER VRZ',
        'unit' : 5,
        'tahun' : 2022,
        'kapasitas' : 7,
        'harga' : 1000000
    }]

cartSewa = []

def menu1():
    while True :
        menu1 = input('''
    ++++++++++ Daftar Menu 1 ++++++++++

    1. Daftar Seluruh Mobil
    2. Kembali ke Menu Utama

    Masukkan Pilihan Menu : ''')
        if(menu1 == '1' ):
            daftarMobil()
        elif(menu1 == '2' ) :
            break
        else:
            print('''
    ================================
    Masukkan Pilihan Dengan Benar!!!
    ================================
            ''')

def daftarMobil():
    print('''
    ======================================================================
                       Daftar Mobil Alfi Rent Car Bandung
    ======================================================================
    Index|Jenis Mobil\t|Unit Tersedia\t|Tahun\t|Kapasitas|Harga Sewa/Hari''')
    for i in range(len(listMobil)) :
        print(f"\t{i}|{listMobil[i]['mobil']}\t|{listMobil[i]['unit']}\t\t|{listMobil[i]['tahun']}\t|{listMobil[i]['kapasitas']}\t  |{listMobil[i]['harga']}     ")

def addMobil() :
    daftarMobil()
    while True :
            namaMobil = input('Masukkan jenis mobil yang akan ditambahkan : ').upper()
            for i in range(len(listMobil)) :
                if namaMobil == (listMobil[i]['mobil']) :
                    x = 1
                    if x == 1 :
                        print('''
    =======================================
    Jenis Mobil Sudah Tersedia Dalam Daftar
    ======================================= ''')
                        break
                    else:
                        continue
            else :
                unitMobil = int(input("Masukkan Jumlah Unit Mobil : "))
                tahunMobil = int(input('Masukkan Tahun Mobil : '))
                kapasitasMobil = int(input('Berapa Kapasitas Mobil : '))
                hargaMobil = int(input("Masukkan tarif harga Sewa harian : "))
                listMobil.append({
                    'mobil' : namaMobil,
                    'unit' : unitMobil,
                    'tahun' : tahunMobil,
                    'kapasitas' : kapasitasMobil,
                    'harga' : hargaMobil
                })
                daftarMobil()
                print('''
    =======================================================================
                        Data Daftar Mobil Telah Diupdate!!!
    =======================================================================''')
                break
    return

def hapusMobil() :
    daftarMobil()
    while True :
        indexMobil = int(input("Masukkan Index Jenis Mobil yang Akan Dihapus : "))
        makeSure = input("Apakah anda yakin untuk menghapus data tersebut? (Y/N) ").upper()
        if (makeSure == 'Y') :
            del listMobil[indexMobil]
            daftarMobil()
            print('''
    =======================================================================
                            Data Berhasil Dihapus!!!
    =======================================================================
            ''')
            break
        else:
            continue

def rentMobil() :
    daftarMobil()
    while True :
        indexMobil = int(input("Masukkan index Mobil yang akan disewa : "))
        if indexMobil in range(len(listMobil)) :
            cartSewa.append({
                'mobil' : listMobil[indexMobil]['mobil'],
                'unit' : listMobil[indexMobil]['unit'],
                'tahun' : listMobil[indexMobil]['tahun'],
                'kapasitas' : listMobil[indexMobil]['kapasitas'],
                'harga' : listMobil[indexMobil]['harga']
            })
            break
        else :
            print('''
    =======================================================================
                    Index dan jenis mobil tidak tersedia!!!
    =======================================================================
        ''')
            continue

    while True:
        brpUnit = int(input('Berapa Unit yang akan anda sewa : '))
        sewa = int(input('Durasi anda akan menyewa mobil ... Hari : '))
        print('Daftar Sewaan : ')
        print('Jenis Mobil\t|Unit\t| Durasi(Hari) | Harga/Hari')
        for item in cartSewa :
            print(f"{item['mobil']}\t|{brpUnit}\t| {sewa}\t       | {item['harga']}") 
        checker = input('Apakah anda akan menyewa jenis mobil yang lain? (Y/N) : ').upper()
        if(checker == 'Y') :
            rentMobil()
        else :
            break

    while True :
            sewaSupir = input('Apakah anda ingin ditemani driver(Rp.200.000)/Lepas Kunci (Y/N) : ').upper()
            if(sewaSupir == 'Y') :
                sewaSupir = 200000
                break
            else :
                break

    print('Daftar Sewaan : ')
    print('Jenis Mobil\t|Unit\t| Durasi(Hari) | Harga/Hari')
    totalHarga = 0
    for item in cartSewa :
        print(f"{item['mobil']}\t|{brpUnit}\t| {sewa}\t       | {item['harga']}") 
        totalHarga = brpUnit * item['harga'] * sewa + sewaSupir
    while True :
        print(f'''
        ---------------------------------------
        Total yang harus dibayar : {totalHarga}
        ---------------------------------------''')
        jmlUang = int(input('Masukkan jumlah uang pembayaran : '))
        kembali = jmlUang - totalHarga
        if(jmlUang > totalHarga) :
            print(f'''
            Uang Kembalian anda Sebesar = {kembali}

                    ==============
                    Terima Kasih<3
                    ==============''')
            cartSewa.clear()
            break
        elif(jmlUang < totalHarga) :
            print(f'''
            Uang pembayaran anda kurang sebesar = {kembali}
            
                ======================================
                Silahkan melakukan pembayaran kembali!
                ======================================
            ''')
            continue
        else:
            print('''
            ==============
            Terima Kasih<3
            ==============''')
            cartSewa.clear()
            break

while True :
    daftarPilihan = input('''
    Selamat Datang di Rental Mobil Alfi

    Pilihan Menu Aplikasi :
    1. Daftar Mobil
    2. Update Jenis Mobil
    3. Delete Jenis Mobil
    4. Sewa Mobil
    5. Exit

    Masukkan angka Menu yang ingin dijalankan : ''')
    if(daftarPilihan == '1' ):
        menu1()
    elif(daftarPilihan == '2' ) :
        addMobil()
    elif(daftarPilihan == '3' ) :
        hapusMobil()
    elif(daftarPilihan == '4' ) :
        rentMobil()
    elif(daftarPilihan == '5') :
        break
    else:
        print('''
    =====================================
    Masukkan Pilihan Menu Dengan Benar!!!    
    =====================================
    ''')