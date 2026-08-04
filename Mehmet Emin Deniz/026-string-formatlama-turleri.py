# formatın bazı türleri devam:

# {: } methodu ==> - sayılarda - 'yi belirtir 
# + sayılarda + sayıdan önce bir boşluk bırakır
text = "Sıcaklıklar bu aylarda {: } ve {: } derece arasında seyreder."
print(text.format(-5,+5))

# {:,} binlikleri ayırıcı olarak kullanılır.
# her bir binlikte bir vürgül atar.

text1 = "Bu arabanın fiyatı {:,} TL'dir"
print(text1.format(12750000)) # 12,750,000

# {:_} binlikleri ayırıcı olarak kullanılır.
# her bir binlikte bir _ atar.

text2 = "Bu arabanın fiyatı {:_} TL'dir"
print(text2.format(12750000)) # 12_750_000

# {:b} binary formunda yazar
text3 = "Binary versiyonu {0} => {0:b}" # ilk parametre sayının kendisi ikincisi binary format
print(text3.format(6))

# {:c} unicode formunda yazar
text4 = "Unicode versiyonu {0} => {0:c}" # ilk parametre sayının kendisi ikincisi unicode format
print(text4.format(199)) # Ç

# {:d} decimal formunda yazar
text5 = "Bizim {:d} çocuğumuz var"
print(text5.format(0b101)) # 0b => binary olduğunu söyler 
# 0x ile hexadecimal bu ön ektir belirtmek için kullanıyoruz.

# {:e} bilimsel formatta sayı yazar
text6 = "Bizim {:e} çocuğumuz var"
print(text6.format(6))
# {:E} formatı da var

# {:f}float gösterimi
text7 = "Bu ürünün fiyatı {:.2f} liradır"
print(text7.format(100))
# önüne .(sayı)f şeklinde virgülden sonra kaç sıfır yazdırılacağını belirtebiliriz.
# varsayılan olarak 6 basamak getirir. C'Deki gibi.
# zaten python C tabanlıdır.

# inf : infinity / sonsuzluk
# nan : nat a number / bir sayı değil
x = float('nan') # nan
text8 = "Fiyat => {:F} Türk lirasıdır" # büyük F ile bunları yazdırır.
print(text8.format(x))

#  {:o} octal format 8'lik sayı sistemi:
text9 = "Oktal versiyonu {0} sayısının => {0:o}"
print(text9.format(19))

#  {:x} hexadecimal format 16'lik sayı sistemi:
text10 = "Hexadecimal versiyonu {0} sayısının => {0:x}"
print(text10.format(79))
# büyük X ile de yazılabilir. çıktı da büyük harfler yazar.

# {:n} number format normal sayı formatı
text11 = "Okul numaran => {:n}"
print(text11.format(350))

# {:%} yüzdesel format.
text12 = "Oy oranı => {:.0%}"
print(text12.format(0.51))