#eğer bir değişkenin içine birden çok satırda veri yazacaksak """ xxxx """ arasına yazmamız lazım (3 tane tek tırnak arasına da olur)
text=""" this is so good 
life is good 
........
........"""
print(text) 

#list veya arraylerde inex 0 dan başlar 


#stringler de birer array dir . her bir karakter her bir harf birer indextir .(boşluklar , işaretler dahil)

#---------------------------------------stringlerde döngü----------------------------------------------------------
#stringler birer array olduğundan döngüyle bir stringdeki harflerin arasında dolaşabiliriz.
text="python uzun bir dildir"
for x in text :
    print(x)
#text i x in içine boşalt ve teker teker harfleri yazdırır.


#stringin uzunluğunu bulmak için len() fonksiyonu kullanırız.
#belirli bir karakterin bir stringin içinde bulunup bulunmadığını aramak için in kullanırız.
print("uzun" in text)  #varsa true yoksa false döndürür.

search="dildir"
print(search in text) #değişkene atayıp da aratma yapabiliriz 
# içinde olmayanı aramak için de not in kullanırız.
#yoksa true varsa false döner.

#stringlerde dilimleme 
yazi="python çok geniş kapsamlıdır"
print(yazi[1:5]) #1.indexten 5. indexe kadar 1 dahil, 5 dahil değil 1,2,3,4 alır çıktı:ytho olur
#başlangıç değeri girmezsem doğrudan : ile başlarsam 0 dan başlar 
#başlangıç indexi girip bitiş indexi girmezsem de başlangıçtan sonuna kadar ilerler.
#negatif değerlerde durumlar tam tersidir . sağdan başlar ,başlangıç değeri sağda dahil olan , bitşi değeri soldaki dahil olmayandır .


#stringlerde değiştirme 
print(text.upper()) #hepsini büyük harf yapar 
print(text.lower()) #hepsini küçük harf yapar 
print(text.replace("P","T"))#ilk harfi ikinci har ile değiştirir.
print(text.split(","))# "," e göre ayırma işlemi yapar .

