# == eşit mi sorgulaması yapar.
# = bu ise atama operatörüdür.
# = değeri değişkene atar == değerleri karşılaştırır.

x = 7
y = 19
print(x == y)  # False verir eşit değiller çünkü.

z = 7
print(x == z)  # True verir çünkü eşitler.

# karşılaştırma operatörleri genelde koşullu ifadelerde kullanılır. Örneğin if, while gibi.

if x == z:
    print(f"{x} ve {z} eşittir.")  # Bu satır çalışır çünkü x ve z eşit.
else:
    print(f"{x} ve {z} eşit değildir.")  # Bu satır çalışmaz çünkü x ve z eşit.

if x == y:
    print(f"{x} ve {y}   eşittir.")  # Bu satır çalışmaz çünkü x ve y eşit değil.
else:
    print(f"{x} ve {y} eşit değildir.")  # Bu satır çalışır çünkü x ve y eşit değil.

# =!= eşit değil mi sorgulaması yapar.
# eşit değil ise true dçöner, eşit ise false döner.
x = 7
y = 19
print(x != y)  # True verir çünkü eşit değiller.

z = 7
print(x != z)  # False verir çünkü eşitler.

if x != z:
    print(f"{x} ve {z} eşit değildir.")  # Bu satır çalışmaz çünkü x ve z eşit.
else:
    print(f"{x} ve {z} eşittir.")  # Bu satır çalışır çünkü x ve z eşit.


# > ve < büyüktür ve küçüktür sorgulaması yapar.
x = 7
y = 19
print(x > y)  # False verir çünkü x y den küçük.
print(x < y)  # True verir çünkü x y den küçük.

if x > y:
    print(f"{x} {y} den büyüktür.")  # Bu satır çalışmaz çünkü x y den küçük.   
else:
    print(f"{x} {y} den küçüktür.")  # Bu satır çalışır çünkü x y den küçük.

# =>= ve <= büyük eşit ve küçük eşit sorgulaması yapar.
x = 7
y = 19
z = 7
print(x >= y)  # False verir çünkü x y den küçük.
print(x <= y)  # True verir çünkü x y den küçük.
print(x >= z)  # True verir çünkü x z ye eşit.

if x >= y:
    print(f"{x} {y} den büyüktür veya eşittir.")  # Bu satır çalışmaz çünkü x y den küçük.
else:
    print(f"{x} {y} den küçüktür.")  # Bu satır çalışır çünkü x y den küçük.
    