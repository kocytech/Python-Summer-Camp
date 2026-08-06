# bilgisayar dünyasında işler 1 ve 0 ile döner
# bu 1 ve 0 lar üzerinde yaptığımız bitsel işlemler 
# bu işlemleri yaptığımız operatörlere de bitsel operatör deriz.

# and kapısı mantıktaki ve kapısı
# 1 - 1 = 1
# 1 - 0 = 0
# 0 - 1 = 0
# 0 - 0 = 0
# iki durum da 1 olduğunda 1 verir

# or kapısı mantıktaki veya kapısı
# 1 - 1 = 1
# 1 - 0 = 1
# 0 - 1 = 1
# 0 - 0 = 0
# en az bir tane 1 varsa 1 verir

# bitsel and atama operatörü &=
# bitsel düzeyde and işlemi uygular
x = 7
x &= 12
print(x) # 4 verir

# 7 =  (00000111)
# 12 = (00001100)
# &= > (00000100)
# 4 =  (00000100)
# 4 çıkmış oldu 

# bitsel or atama operatörü |=
# bitsel düzeyde or işlemi uygular
y = 7
y |= 12
print(y) # 15 verir

# 7 =  (00000111)
# 12 = (00001100)
# |= > (00001111)
# 15 = (00001111)
# 15 çıkmış oldu 

# bitsel xor atama operatörü ^=
# bitsel düzeyde xor işlemi uygular
z = 7
z ^= 3
print(z) # 4 verir

# 7 =  (00000111)
# 3 =  (00000011)
# ^= > (00000100)
# 4 =  (00000100)
# 4 çıkmış oldu     

