# pythonda \r ile yükleme barı:
import time # time modülünü import ettik. time modülü ile bekleme süresi verebiliriz.
for i in range(101): # 0'dan 100'e kadar olan sayıları yazdırır.
    time.sleep(0.1) # 0.1 saniye bekletir.
    print("\rYükleniyor... %d%%" % i, end="") # her seferinde aynı satırda yazdırır. 
    # her defasında bir az önceki yazdığını siler ve yeni yazdığını yazar.
    # sayılar 1er 1 artar ve %100 olunca döngü biter.
    # sanki yükleme barı gibi bir görüntü oluşur.