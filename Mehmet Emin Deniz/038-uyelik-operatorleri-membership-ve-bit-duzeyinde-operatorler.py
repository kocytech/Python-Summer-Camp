# in ve not in üyelik operatörleri, 
# bir öğenin bir seri içinde olup olmadığını kontrol etmek için kullanılır.

meyveler = ["elma", "armut", "muz", "çilek"]

print("elma" in meyveler)  # True, çünkü "elma" listede var
print("portakal" in meyveler)  # False, çünkü "portakal" listede yok

# aranan_deger in aranacak_liste 
# şeklinde kullanılır. Eğer aranan_deger, 
# aranacak_liste içinde varsa True döner, yoksa False döner.

# not in operatörü ise, bir öğenin bir seri içinde olmadığını kontrol etmek için kullanılır.
# yok ise True döner, varsa False döner.

print("portakal" not in meyveler)  # True, çünkü "portakal" listede yok
print("elma" not in meyveler)  # False, çünkü "elma" listede var


# bitwise operatörler, sayısal değerler üzerinde bit düzeyinde işlemler yapmak için kullanılır.
# bitwise için & kullanılır. Bu operatör, iki sayının bitlerini karşılaştırır 
# ve her iki bit de 1 ise 1 döner, aksi takdirde 0 döner.

a = 6  # 110 in binary
b = 3  # 011 in binary
c = a & b  # 010 in binary (bitwise AND)
print(c)  # 2, çünkü sadece ikinci bit her iki sayıda da 1

# bitwise or operatörü | kullanılır. Bu operatör, iki sayının bitlerini karşılaştırır
# ve herhangi bir bit 1 ise 1 döner, aksi takdirde 0 döner.
d = a | b  # 111 in binary (bitwise OR)
print(d)  # 7, çünkü herhangi bir bit 1 ise 1 döner

# bitwise xor operatörü ^ kullanılır. Bu operatör, iki sayının bitlerini karşılaştırır
# ve sadece bir bit 1 ise 1 döner, aksi takdirde 0 döner.
e = a ^ b  # 101 in binary (bitwise XOR)    
print(e)  # 5, çünkü sadece bir bit 1 ise 1 döner

# zerofill left shift operatörü << kullanılır. Bu operatör, bir sayının bitlerini sola kaydırır ve sağa sıfır ekler.
f = a << 1  # 1100 in binary (left shift)
print(f)  # 12, çünkü sayıyı 1 sola kaydırır ve sağa sıfır ekler

# zerofill right shift operatörü >> kullanılır. Bu operatör, bir sayının bitlerini sağa kaydırır ve sola sıfır ekler.
g = a >> 1  # 011 in binary (right shift)
print(g)  # 3, çünkü sayıyı 1 sağa kaydırır ve sola sıfır ekler

# 2nin kuvveti olan sayılar için, << ve >> operatörleri ile çarpma ve bölme işlemleri yapılabilir.

# bitwise not operatörü ~ kullanılır. Bu operatör, bir sayının bitlerini tersine çevirir.
h = ~a  # 001 in binary (bitwise NOT)
print(h)  # -7, çünkü sayının bitlerini tersine çevirir ve negatif bir sayı döner

# sign bit işareti, sayının pozitif mi yoksa negatif mi olduğunu belirten bittir.
# 0 ise pozitif, 1 ise negatif sayıyı temsil eder.

# operaötlerin öncelik sıralaması:
# 1. Parantezler ()
# 2. Üyelik operatörleri (in, not in)
# 3. Bitwise operatörler (&, |, ^, <<, >>
# aritmetik operatörler (+, -, *, /, //, %, **)
