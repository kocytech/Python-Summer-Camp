# strip : başında ve sonunda boşluklar var onları kaldırır
text = "....BMW    "
sonuc = text.strip()
print("araba markası:", sonuc)

# lstrip ve rstrip : sağdan soldan silme
# strip soy kaldır gibi bir anlamı var
print(text.rstrip())
print(text.lstrip())

# stripe ile sadece boşluk değil istediğimiz şeyi de kaldırtabiliriz
foo = text.lstrip(".B")
print(foo) # MW

# maketrans() => belirtilen karakterleri değiştirmek için kullanılır.
foo2 =  "Merhaba, Python"
sonuc = str.maketrans("M","S") # make trans ile:
# çevirme kurallarını beliritiriz.
print(foo2.translate(sonuc)) # çevirme işlemi yaptırırız parametre olarak:
# kuralları belirlediğimiz değişkeni veririz.

# dict türü ile de maketrans parametresi verebiliriz
myDict = {80:84, 75:65, 108:65} # unicode olarak birden fazla değer de verebilirz
textx = "Hello Python"
result = str.maketrans(myDict)
print(textx.translate(result))

# maketrans 3 parametre alır. 
# 3. parametre ile kaldırmak istediğimiz karakterleri belirtiriz.

texty = "Hello Python"
x = "PHo"
y = "Tmi"
z = "l"
resulty = str.maketrans(x,y,z)
print(texty.translate(resulty))

# partition() stringin 3 parçaya bölündüğü bir tuplle veri türü döndürür.
# başlangıç - **orta** - son
text2 = "Her gün python çalışıyorum"
text3 = text2.partition("python")
print(text3)
# olmayan bir kelime verildiğinde tüm stringi ilk elemna atar kalanları boş bırakır.

# replace methodu bir string değerini başka bir şeyle değiştirmeye yarar
text4 = "Ben her gün çilek yerim"
text5 = text4.replace("çilek", "muz")
print(text5)

text6 = "Ben her gün çilek çilek çilek çilek çilek çilek yerim"
text7 = text6.replace("çilek", "muz", 2) # 3. parametre kaç tanesini değiştirileceğini belirtir.
print(text7)