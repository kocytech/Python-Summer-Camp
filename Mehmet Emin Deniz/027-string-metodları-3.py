# isdigit() metodu => tüm karakterler rakam ise true döndürür
text = "23423523"
sonuc = text.isdigit()
print(sonuc) # true
# örneği yaş istenilen bir yerde sayı girildi mi girilmedi mi diye kontrol etmek için.
# üstsel ifadeleri de kabul eder.
x = "\u0031" # 1 unicode'a göre
y = "\u00B2" # üstsel 2
print(x.isdigit()) # true
print(y.isdigit()) # true

# isidentifier() tanımlayıcı demektir
# sadece alfanümerik ve _ içeriyorsa isidentifier'dır.
# yani tanımlayıcıdır. değilse tanımlayıcı değildir.
# geçerli bir tanımlayıcı sayı ile başlayamaz
# geçerli bir tanımlayıcı boşluk içeremez
a = "MehmetEmin"
b = "Python3"
c = "3Python"
d = "Mehmet Emin"
e = "Mehmet_Emin"
f = "Mehmet-Emin"
print(a.isidentifier()) # true
print(b.isidentifier()) # trure
print(c.isidentifier()) # false
print(d.isidentifier()) # false
print(e.isidentifier()) # true
print(f.isidentifier()) # false

# islower => tüm harfler küçük karakter ise
# isupper => tüm harfler büyük ise

# isnumerik() => tüm karakterler sayı mı?
foo = "23435"
sonuc = foo.isnumeric()
print(sonuc)
# üstsel ifadeleri de numerik görür
# -'li ve float sayıları numerik olarak görmez.
# içinde sadece rakamları kabul eder. - yi ve . yı numerik değil olarak kabul eder.

x = "\u0031" # 1 unicode'a göre
y = "\u00B2" # üstsel 2
print(x.isnumeric()) # true
print(y.isnumeric()) # true

# isprintable() ==> stringdeki tüm karakterler yazdırılabiliyor mu?
# output veriyor mu ?  mesela kaçış karakterler \n \t output'da gözükmez.
isim = "Mehmet Emin Deniz"
isim2 = "Mehmet\nEmin\nDeniz"
sonuc2 = isim.isprintable()
sonuc3 = isim2.isprintable()
print(sonuc2) # true
print(sonuc3) # false 

# isspace() ==> boşluk kontrolü yapar içindeki her karakteri boşluk ise true döndürür.
foobar = "Mehmet Emin Deniz"
foobar1 = "     "
print(foobar.isspace()) # false
print(foobar1.isspace()) # true
 
# title() => her bir kelimenin baş harfini büyük yaoar
# istitle() => her kelimenin ilk harfi büyük mü kontrol eder true döndürür
foobar2 = "Bu Kodları Mehmet Emin Deniz Yazdı"
print(foobar2.istitle()) # true 

# join string methodu
isimler = ("Fehmi", "Murat", "Yunus", "Emin", "Deniz") # tupple liste türü
tek_liste = ",".join(isimler) # burdaki virgül bir ayırıcıdır. 
# yeni listeyi oluştururken eklenen elemanların arasına bunu ekle demektir.
print(tek_liste)
# virgül yerine başka bir şey de koyabiliriz.

personel_bilgileri = {"isim":"Emin", "ülke":"Türkiye"}  # dict veri türü. 
# key - value / anahtar değer ikilisi
ayırıcı_karakter = ", "
yeni_liste = ayırıcı_karakter.join(personel_bilgileri)
yeni_liste2 = ayırıcı_karakter.join(personel_bilgileri["isim"])
print(yeni_liste)
print(yeni_liste2) # isim değerini alır 

# ljust ve rjust metodlar sola veya sağa yaslanacak formatı
foobar3 = "çilek"
sonuc4 = foobar3.ljust(19) # 19 boşluk ayır stringi sol tarafına yasla
sonuc5 = foobar3.rjust(19) # 19 boşluk ayır stringi sağ tarafına yasla
print("ljust: ", sonuc4)
print("rjust: ", sonuc5)
# boşluk yerine farklı karakterlerle de doldurabiliriz 
sonuc6 = foobar3.ljust(10, "*")
print(sonuc6) # çilek*****