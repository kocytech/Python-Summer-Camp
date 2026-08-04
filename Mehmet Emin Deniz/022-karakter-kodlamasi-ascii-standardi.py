# unicod ve ascii cod farkları.
# bilgisayarlar üzerinde elektrik geçen devrelerdir.
# üzerinden elektrik geçmiyorsa 0V ===> 0
# üzerinden elektrik geçiyorsa 5V ===> 1
# bilgisayarlarla biz metinsel bir iletişim kurabilmek için
# ASCII tabloyu kullanırız.
# bilgisayarlar bitsel değerlerin ascii karşılıklarına göre sonuç üretirler.
# ord methodu ASCII değer verir
# print(ord("A"))
# bin methodu binary karşılığını verir
# print(bin(70))
# bir sinyali karaktere karakteri bir sinyale dönüştürme olayı:
# karakter kodlama = character encoding
# hangi karakterin hangi değerle eşleşeceğini ascii tabloya göre belirlenir
# ibm veri alışverişini sağlamak için bunu standartlaştırdı.
# ascii tabloda sadece ingilizce karakterler yer alır
# bit_length() bit uzunluğunu verir
# print((127).bit_length())
# 8 bitle en fazla 256 karakter tutulabiliyordu.
# bu da bir yerden sonra yetersiz gelecekti.
# C ascii kullanıyor. türkçe karakter kabul etmiyor.
# C'nin eski olmasından kaynaklı bu da biraz. 
# o zamanlar unicode yoktu.

# text = "Ç"
# sonuc = text.encode("ascii")
# print(sonuc)

# ascii hiç bir zaman 128i geçmedi
# genişletilmiş ascii ler ise standırtılmamış şekilde genişletilmiştir.
# ama bunların hiç biri tüm dilleri kapsayamamıştır.