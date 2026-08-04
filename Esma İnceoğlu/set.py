#set(küme)
#Set matematikteki kümeler gibidir.
#en önemli özelliği aynı elemanı iki kez tutmaz , tekrar edenleri siler .
sayilar={1,2,3,4}

#eleman ekleme 
sayilar.add(5)

#eleman silme 
sayilar.remove(3)

#set sıralı değildir , yani index yoktur çıktı bazen 1,2,4,3 bazen 4,1,2,3 ... gibi olur 
#sayilar[0] yapamayız hata verir.

#list ile farkı 
#liste tekrarları tutar , set tekrarları siler 