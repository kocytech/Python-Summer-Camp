# ascii standarta göre bir karakter bir byte ile ifade edilr.
# bunun özel bir nedeni yoktur.
# aynı bir deste 10 tanedir gibi kabul görmüş bir şeydir
# 256'dan sonra 1 byte yetersiz kalır.
# bunun sonucunda unicode ortaya çıktı
# universal code = evrensel kod
# 8. biti ülkeler genişletilmiş ascii yapmak için kullandı
# ama bu da standartlaşmaya ters gelişti.
# bunu önlemek için evrensel bir standart olan unicode ortaya çıktı
# unicode'da ascii üzerine inşa edilmiştir.
# önceki sistemlere de uyumlu olsun.
# 256 ve üzerindeki karakterler de artık kullanılabiliyordu.
# unicode 16 bitlik bir sistemdi ilk çıktığında
# her karakter benzersiz ve tek bir sayısal karşılığı vardır.
# içinde farklı kodlama sistemlerini de kullanır.
# utf-8 sayesinde alan israfının önüne geçilir.

# print('ç'.encode("utf-8")) # utf-8'e göre binary'e çevirir
# c3a7
# print(int("c3a7", 16)) # 16'lık halini 10 luk tabana göre döndürür
# 50087
# print(bin(50087)) # onluk tabandaki halinin bit karşılığını verir
# 0b1100001110100111
# print((0b1100001110100111).bit_length())
# print((50087).bit_length())

# encode ve decode:
text = "\x50\x79\x74\x6F\x6E"
sonuc = text.encode("ascii") # ascii karakter koduyla encode'la
sonuc2 = sonuc.decode("ascii") # decode et yani çözümle

print(sonuc, "türü", type(sonuc)) # Python, bytes
print(sonuc2, "türü", type(sonuc2)) # Python, str

# encode ve decode 2 parametre alır 
# ilk parametere türünü belirtir. encoding/decoding
# ikinci parametre hatalar için kullanılır errors

# strict modu katı moddur.
# backslashreplace ==> parametresi hataları \ ile doldurur.
# ignore ==> görmezden gel
# namereplace ==> orda ne olduğunu açıklar
# replace ==> temsil edilmeyenler yerine ? bırakır 
# xmlcharrefreplace ==> temsil edilmeyen harfler yerine xml karşılığını verir

isim = "EMİN" # büyük İ
foo = isim.encode(encoding="ascii", errors="backslashreplace")
print(foo)

isim = "EMİN" # büyük İ
foo = isim.encode(encoding="ascii", errors="ignore")
print(foo)

isim = "EMİN" # büyük İ
foo = isim.encode(encoding="ascii", errors="namereplace")
print(foo)

isim = "EMİN" # büyük İ
foo = isim.encode(encoding="ascii", errors="replace")
print(foo)

