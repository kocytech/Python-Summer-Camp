# mantıksal operatörler ve kimlik operatörleri

# = mantıksallar = 
# and, or, not

# = kimlik operatörleri =
# is, is not

# mantıksal operatörler koşullu ifadeleri birleştirmek için kullanılır.

from turtle import pu


x = 7
y = 3
if x > 5 and x < 10: # ikisi de doğru ise True döner
    print("x 5 ile 10 arasında bir sayıdır.")

if x < 5 or y < 10: # ikisinden biri doğru ise True döner
    print("x 5 ile 10 arasında bir sayı değildir.")

# alınan puana göre öğrencinin geçip geçmediğini kontrol eden bir program yazalım.
puan = int(input("Lütfen puanınızı giriniz: "))

if puan >= 0 and puan <= 100:
    if puan >= 50 and puan <= 70:
        print("Tebrikler, geçtiniz, orta bir başarı gösterdiniz.")
    elif puan > 70 and puan < 100:
        print("Tebrikler, geçtiniz, yüksek bir başarı gösterdiniz.")
    elif puan == 100:
        print("Tebrikler, geçtiniz, mükemmel bir başarı gösterdiniz. Tam puan aldınız.")
    else:
        print("Üzgünüz, geçersiz puan girdiniz.")
else:
    print("Girilen puan geçersizdir.")

# not operatörü, bir koşulun tersini almak için kullanılır. 

t = 5 
print(not( t > 10 and t < 15)) # normalde içerisi False dönerken not operatörü ile True döner sonucu

if not(puan >= 50):
    print("Üzgünüz, geçemediniz.")


# is kimlik operatörü, iki değişkenin aynı nesneye referans verip vermediğini kontrol eder.
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, çünkü farklı nesneler
print(a is c)  # True, çünkü aynı nesneye referans veriyor
print(a is not b)  # True, çünkü farklı nesneler    

# içeriklerinin aynı olması aynı nesne olduğu anlamına gelmez. 
# is operatörü, iki değişkenin aynı nesneye referans verip vermediğini kontrol eder.
# atama ile değişkene bir nesne referans verilir.
# o zaman aynı nesne olur.

# is not ise aynı nesneye referans verip vermediğini kontrol eder 
# eğer farklı nesnelere referans veriyorsa True döner.
# is'in tam tersi gibi düşünebiliriz.

