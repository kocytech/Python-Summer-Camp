#string formatlama
age=21
name="esma"
text="My name is {} , I am {} " .format(name,age)
print(text)
#süslü paarantezler içinde index de girebiliriz 0--> name e karşılıktır 1--> age e karşılıktır.

#f-string kullanımı 
age=21
name="esma"
text=f"My name is {name} , I am {age} " 
print(text)


#string metodları 
#capitalize() metodu string içindeki cümlenin ilk harfini büyük yapar .
#casefold() metodu ise lower gibi harfleri küçük yapar . farkı lower dan daha fazla karakteri küçük yapar yani daha güçlüdür.özel karakterleri de küçük yapabilir.
#title() her bir kelimenin ilk harfini büyür yazar.rakam gördükten sonraki kısmınd ilk harfini büyük yazar.
#swapcase() büyükleri küçükk , küçükleri büyük yapar 
#islower() küçük harf mi sorusnu sorar küçükse true döndürür.
#isupper() hepsi büyük harf ise true döndürür.
#center() ortalar parantezin içine girdiğimiz değere göre . , koyup bir parametre daha girersek *,? gibi ona göre ortalar kenarlara ikinci parametreyi koyar 
 