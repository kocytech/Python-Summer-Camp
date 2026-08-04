# lower ve upper metodu ile stringin tüm karakterlerini küçük veya büyük harfe çevirebiliriz.
text = "Python Programlama Dili"    
print(text.lower()) # tüm karakterler küçük harfe çevrilir.
print(text.upper()) # tüm karakterler büyük harfe çevrilir.

# capitalize metodu ile stringin ilk karakterini büyük harfe çevirebiliriz.
print(text.capitalize()) # ilk karakter büyük harfe çevrilir.

# casefold metodu ile stringin tüm karakterlerini küçük harfe çevirir ve büyük/küçük harf farkını ortadan kaldırır.
text = "Python Programlama Dili"
print(text.casefold()) # tüm karakterler küçük harfe çevrilir.
# lower ile casefold arasındaki fark: lower metodu sadece küçük harfe çevirir, casefold metodu ise büyük/küçük harf farkını ortadan kaldırır.
# casefold daha güçlü ama daha yavaştır

# title metodu ile stringin her kelimesinin ilk karakterini büyük harfe çevirebiliriz.
text = "python programlama dili"
print(text.title()) # her kelimenin ilk karakteri büyük harfe çevrilir.
# bir rakamı gördükten sonra gelen karakterler de büyük harfe çevrilir. 

# swapcase metodu ile stringin tüm karakterlerinin büyük/küçük harflerini tersine çevirebiliriz.
# swap takas demektir
text = "Python Programlama Dili"
print(text.swapcase()) # tüm karakterlerin büyük/küçük harfleri tersine

# islower ve isupper metodu ile stringin tüm karakterlerinin küçük veya büyük harf olup olmadığını kontrol edebiliriz.
text = "python programlama dili"
print(text.islower()) # tüm karakterler küçük harf ise True döner.
text = "PYTHON PROGRAMLAMA DILI"
print(text.isupper()) # tüm karakterler büyük harf ise True döner.

# center metodu ile stringin ortalanmasını sağlayabiliriz.
text = "Python"
print(text.center(20)) # string 20 karakterlik bir alanın ortasında yer alır.

# center ikinci bir parametre daha alabilirr
# boşluklar yerine başka bir karakter ile doldurulabilir.
text = "Python"
print(text.center(20, "*")) # string 20 karakterlik bir alanın ortasında yer alır ve boşluklar * ile doldurulur.

# terminalde daha güzel çıktılar sağlayabiliriz.