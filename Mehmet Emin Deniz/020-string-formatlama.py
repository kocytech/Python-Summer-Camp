# string ile bir integer veya float gibi bir sayıyı birleştirmek istiyorsak bunu string formatlama ile yapabiliriz.
age = 25
text = "Benim yaşım" + str(age) + "dir." # integer olan age değişkenini stringe çevirdik.   

# format metodu ile string formatlama:
text = "Benim yaşım {} dir.".format(age) # {} içine age değişkeni yerleştirilir.

# iki parametre de ekleyebiliriz:
name = "Necip"
text = "Benim adım {} ve yaşım {} dir.".format(name, age) 
# {} içine name ve age değişkenleri yerleştirilir.    

# format metodu ile string formatlamada index numarası da verebiliriz:
text = "Benim yaşım {1} dir. Adım {0}.".format(name, age)   

# yukardaki yöntem eski bir yöntemdir. 
# Python 3.6 ve sonrası için f-string yöntemi kullanılabilir.
# f-string yöntemi ile string formatlama:

print(f"Benim adım {name} ve yaşım {age} dir.") 
# f-string yöntemi ile değişkenler {} içine yazılır.    

# formatlama sayesinde string içinde değişkenleri kolayca kullanabiliriz.

araba_fiyat = 10.0000
print(f"Arabanın fiyatı {araba_fiyat} TL'dir.")

elma_fiyat = 5.0000
print(f"Elmanın fiyatı {elma_fiyat:.2f} TL'dir.") 
# float sayıyı x ondalık basamak ile yazdırmak için :.xf kullanılır.

# ----------------------------------------------------
# vize - final notu hesaplama örneği:

vize_notu = int(input("Vize notun: "))
final_notu = int(input("Final notun: "))
ortalama = (float(vize_notu) * 0.4) + (float(final_notu) * 0.6)

sonuc = f"Vize notunuz: {vize_notu}, \nFinal notunuz: {final_notu}, \nOrtalamanız: {ortalama:.2f}"
print(sonuc)