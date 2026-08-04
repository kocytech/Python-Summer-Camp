text = "Bu ürünün fiyatı sadece {fiyat:.2f} lira!"
print(text.format(fiyat=70))
# {} ==> yer tutuculardır. placeholder 

foo = "Benim ismim {isim}, ben {yas} yaşındayım".format(isim = "Mehmet Emin", yas = 21)
print(foo)

foo2 =  "Benim ismim {0}, ben {1} yaşındayım".format("Mehmet Emin", 21)
print(foo2) # index ile yazdırdığımızda değişken yazmamız gerekmez

foo3 = "Benim ismim {}, ben {} yaşındayım".format("Mehmet Emin", 21)
# index'leri belirtmezsek default olarak kendisi sıralı sıralayacaktır.
print(foo3)

# ======= FORMAT TİPLERİ =======
# biçimlendirme türleri 
# { : < 10} 10 birim boşluk bırak ve sola hizala.
bar = 'Bizim {:<10}  çocuğumuz yok' 
print(bar.format(7)) # yukardaki yere 7'yi yazar ve sola yaslar
print(bar.format("kız")) # yukardaki yere "kız" yazar ve sola yaslar.

# { : > 10} 10 birim boşuk bırak sağa hizala
bar1 = 'Bizim {:>10}  çocuğumuz yok'
print(bar1.format(5))

# { : ^ 10} 10 birim boşluk bırak merkeze hizala
bar2 = 'Bizim {:^10}  çocuğumuz yok'
print(bar2.format("erkek"))

# { : = 10} matematiksel işaretini en sola yerleştirir.
# + olanları özel olarak belirtmez ekstradan.
foobar = "Sıcaklık bugün {:=10} derece."
print(foobar.format(10)) # işaret belirtmez 
print(foobar.format(-10)) # - yi sola yaslar belirtir

# :- ve :+ biçimlendirmeleri
# - ve + işaretlerini belirtir.
foobar1 = "Sıcaklıklar bu aylarda {:-} ve {:+} derece arasında seyreder."
print(foobar1.format(-5,+5))