#dictionary (sözlük) anahtar değer mantığıyla çalışır.
ogrenci = {
    "ad": "Esma",
    "yas": 21,
    "bolum": "Bilgisayar Mühendisliği"
}

#değere ulaşma
print(ogrenci["ad"])

#yeni eleman ekleme 
ogrenci["okul"] = "KSÜ"

#son hali :
{
    "ad": "Esma",
    "yas": 21,
    "bolum": "Bilgisayar Mühendisliği",
    "okul": "KSÜ"
}

#değeri değiştirme 
ogrenci["yas"] = 22

#eleman silme 
del ogrenci["yas"]
#veya 
ogrenci.pop("yas")

#döngü ile gezme 
for anahtar in ogrenci:
    print(anahtar)

#anahtar ve değeri birlikte 
for anahtar, deger in ogrenci.items():
    print(anahtar, deger)   

ogrenci.keys()#anahtarları verir.
ogrenci.values()#değerleri verir.
ogrenci.items()#anahtar değer çiftlerrini verir.