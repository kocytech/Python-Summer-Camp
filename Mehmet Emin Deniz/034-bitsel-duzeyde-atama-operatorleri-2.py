# right shift atama operatörü >>=
# bitsel düzeyde sağa kaydırma işlemi uygular  
# bitleri sağa kaydırır ve boş kalan bitleri 0 ile doldurur
# bitleri sağa doğru 2 birim kaydırır
# sağa doğru kaydırmak demek matematik olarak bölme işlemine denk gelir
# ikinin kuvveti kadar bölme işlemi yapar

x = 16
# 16 = (00010000)

x >>= 2 
# x = (00000100)
print(x) # 4 verir

# left shift atama operatörü <<=
# bitsel düzeyde sola kaydırma işlemi uygular  
# iki, bitleri sola kaydırır ve boş kalan bitleri 0 ile doldurur
# bitleri sola doğru 2 birim kaydırır
# 2nin kuvvetleri ile çarpma işlemi yapar

y = 5
# y = (00000101)

y <<= 2
print(y) # 20 verir

# kayan bitlerin yerine 0 gelir ve sola kaydırma işlemi yapar.
# 3 bit kaydırmak için
y <<= 3
print(y) # 160 verir
# 5 bit kaydırmak için
y <<= 5
print(y) # 5120 verir

# walrus operatörü (walrus operator) :=
# değişken atama ve değer döndürme işlemini aynı anda yapar 

x = 5
print(x := x + 1) # 6 verir 

print(deneme := 10) # 10 verir
# değişkenin daha önceden tanımlanmasa da olur.


