# right partition
# partition 3 parçaya böleriz.
# tupple verisi olara böler
# 1. veri bölen değer 3. değer
# right partiton ile en son geçen değerden böler
text = "Ben, her gün, python çalışır ve her gün, python da örnekler, yaparım"
result = text.rpartition("python")
print(result)
# ('Ben her gün python çalışır ve her gün ', 'python', ' da örnekler yaparım')

# find() aranan ifade geçiyorsa index'ini geçmiyorsa -1
# index eğer geçmiyorsa hata üretiyordu.
# karar yapıları ile birlikte kullanılır find

sonuc2 = text.find("python")
print(sonuc2)
# rfind ise rpartition gibi en son değeri bulup getirir
sonuc3 = text.rfind("python")
print(sonuc3)
# 2. ve 3. parametreleri vererek aralık belirleyebiliriz.
sonuc4 = text.rfind("e", 15, 30) # 15 ve 30. indexler arasında en sonnuncuyu alır getirir.
print(sonuc4)

# rindex de aynı mantıkta çalışır.

# split : belirtilen ifadede böler ayırır bir *liste* döndürür
# default parametre olrak boşluğu alır
# bir stringdeki kelime sayısını buldurabilir bize.

sonuc5 = text.split()
print(sonuc5)
sonuc6 = text.split(",")
print(sonuc6)
# splitle kaç kez ayırmak istediğimizi de belirleyebiliriz.
sonuc7 = text.split(",", 1)
print(sonuc7)
# rsplit de yine aynı görevi yapar. 

# splitlines stringi bir listeye böler 
# bölme satır sonlarında yapar. 
# \n 'lere göre yapar
# default parametresi false dır
# true parametresi girilirse \n'i de korur listeye yazar.

textx = "Ben, her gün, python çalışır ve her gün, python da örnekler, yaparım"
sonuc8 = textx.splitlines(False)
print(sonuc8)
sonuc9 = textx.splitlines()
print(sonuc9)
sonuc10 = textx.splitlines(True)
print(sonuc10)

# zfill ==> 0 ile doldur demek => zero fill
texty = "70"
sonuc11 = texty.zfill(7) # 7 karakter ayırır boş kalan yerleri 0 ile doldurur
print(sonuc11) # 0000070
