# count komutu
# belirtilen stringde kaç kez geçtiğini belirtir.
text = "deneme bir deneme bir deneme bir"
sonuc = text.count("bir") # "bir" leri sayar
print(sonuc) 
# count 3 parametre alır.
# 1. aranacak değer
# 2. başlangıç değeri
# 3. bitiş değeri

foo = "aaaabbbaaabbaaabbbaabbaabbabab"
print(foo.count("b", 6,15))

# startswith ve endswith
# startswith => string belirtilen değerle başlıyorsa true döndürür
# endswith => string belirtilen değerle bitiyorsa true döndürür.
isim = "emin"
print(isim.startswith("e"), isim.endswith("n")) # true - true 
# startswith ve endswith de 3 parametre alır
# başlangıç ve bitiş indexlerini de verebiliriz.
soy_isim = "deniz"
print(soy_isim.startswith("n",2,5), soy_isim.endswith("i",2,4))

# expandtabs = default tab boşluk değerini değiştiri

foo2 = "e\tm\ti\tn"
print(foo2)
print(foo2.expandtabs(2))
print(foo2.expandtabs(4))
print(foo2.expandtabs(6))
print(foo2.expandtabs(10))

# find methodu = string'de belirtilen değere göre arama yapar
# aranan değerin bulunduğu konumu index numarasını döndürür.
# bulunmazsa eğer eksi bir döndürür.
foo3 = "Python yaz kampı 22. ders videosunu izliyor ve örnekleri yapıyorum."
print(foo3.find("izliyor"))
print(foo3.find("deniyor")) # -1
# find methoduna da başlangıç ve bitiş parametreleri yazabiliriz.

# index methodu da find gibi aranan değerin indexini verir
# bulamazsa find gibi -1 değil hata döndürür.
foo4 = "anamdnöansdaösmdanömaönd"
print(foo4.index("ö"))
# print(foo4.index("k"))

# isalum : stringdeki tüm değerler alfanümerik ise true döndürür
# alfanümerik : sadece harf ve sayılar
foo5 = "denem2134dfer"
foo6 = "adsas343.3^'5"
foo7 = "asdasdasdas"
bar = foo5.isalnum()
bar2 = foo6.isalnum()
print("  isalnum  ".center(40, "*"), "\n",  "foo5:",bar, "--", "foo6:", bar2)

# isalpha : sadece harfleri true olarak dönderir
bar3 = foo5.isalpha()
bar4 = foo6.isalpha()
bar5 = foo7.isalpha()
print("  isalpha  ".center(40,"*"), "\n", "foo5:",bar3, "--", "foo6:", bar4, "--", "foo7:", bar5)

# isascii : sadece ascii karakterleri içeriyorsa true döndürür
foo8 = "deneme"
foo9 = "aasdşiasç"
print("ascii:", "foo8:", foo8.isascii(), "foo9:", foo9.isascii())

# isdecimal : sadece rakam içeriyorsa true döndürür.
foo10 = "32344"
foo11 = "34dff"
print("decimal:", "foo10:", foo10.isdecimal(), "foo11:", foo11.isdecimal())
# unicode değerleri de kontrol eder.