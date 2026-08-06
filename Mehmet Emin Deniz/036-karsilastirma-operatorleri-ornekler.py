# girilen şifrenin doğru olup olmadığını kontrol eden bir program yazalım. 
# Şifre doğru ise "Giriş başarılı", yanlış ise "Giriş başarısız" mesajı verelim

dogru_sifre = "12345"
girilen_sifre = input("Lütfen şifrenizi giriniz: ")

if girilen_sifre == dogru_sifre:
    print("Giriş başarılı")
else:
    print("Giriş başarısız")

# girilen sayının çift mi tek mi olduğunu kontrol eden bir program yazalım.
sayi = int(input("Lütfen bir sayı giriniz: "))

if sayi<0:
    print("Girilen sayı negatif olamaz.")
elif sayi % 2 == 0:
    print("Girilen sayı çifttir.")
else:
    print("Girilen sayı tektir.")

