# programlamada bir şeyin var olup olmadığını kontrol etmek için
# varsa true = 1 yoksa false = 0 değeri alır.
# buna boolen veri türü deriz.
print(7>4) # true verir
print(7<4) # false verir
print(7==4) # false verir

x = 70
y = 19
if x>y:
    print(x, "büyüktür", y)
elif y>x:
    print(y, "büyüktür", x)
elif x==y:
    print(x, "eşittir", y)
else: 
    print("Geçersiz değerler.")

# bool fonksiyonu bool veri türüne dönüştürür ya 0 ya 1

z = bool("python")
t = bool(76)
# 0 hariç her şey true döner
print("z", z)
print("t", t)

# liste veya herhangi dolu başka bir veri gönderdiğimizde bunu true olarak algılar.

meyveler = ["elma", "muz", "çilek", "şeftali"]
print(meyveler, bool(meyveler))

# boş stringi true olarak algılamaz.
print(bool("")) # false
# 0 değeri false verir:
print(bool(0)) # false
# sıfır dışında her şey true döndürür
# true değeri true false değeri false döndürür.
print("true:", bool(True), "\nfalse:", bool(False))

# none değeri false döndürür
print("None:", bool(None))

# boş liste dict ve tuple false dönderir
bos_liste = []
bos_tuple = ()
bos_dict = {}
print("Bos Liste:", bool(bos_liste)) # false
print("Boş Tuple:", bool(bos_tuple)) # false
print("Boş Dict:", bool(bos_tuple)) # false

# fonksiyonlarla da bool değer döndürebiliriz.

def fonksiyonum():
    return True

print(fonksiyonum()) # True döndürür.

# bazı hazır fonksiyonlar da boolen değerler döndürür.

x = 70

print(isinstance(x, int))
print(isinstance(x, str))