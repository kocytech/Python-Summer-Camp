# textin içinde çift tırnak veya tek tırnak kullanmak istiyorsak kaçış karakteri kullanmamız gerekir.
# çift tırnak içinde çift tırnak veya tek tırnak içinde tek tırnak kullanamayız.
# çift içinde tek tırnak veya tek içinde çift tırnak kullanabiliriz.
# bunun sebebi programın derlenirken bir tırnak gördüğünde 
# bu tırnağın bitimi olarak gördüğü ikinci ilk tırnağı alıyor olmasında aynı C'deki gibi mantığı.  
# eğer bunu yapmak istiyorsak \ - backspace - esspace - kaçış karakteri kullanmamız gerekir.

text = "Bunu kesinlikle \"yarın\" getirmelisin" # vurgu için olan tırnak içindekileri
print(text) # Bunu kesinlikle "yarın" getirmelisin

# kaçış karakterleri:
# \n - yeni satır
# \t - tab
# \' - tek tırnak
# \" - çift tırnak
# \r - carriage return
# \b - backspace
# \ooo - octal value
# \xhh - hex value

# backslash bırakmak için:
print("C:\\Users\\Necip\\Desktop") # C:\Users\Necip\Desktop

# alt satıra geçmek için:
print("merhaba\npython") # merhaba  

# imleci başa almak için:
print("merhaba\rpython") # python   
# imleç başa alındığı için merhaba yazısı silinip python yazısı geldi.
# C'de bununla yükleme barı yapabiliyorduk. 
# python'da da aynı mantıkla çalışıyor.

# \t - tab karakteri eklemek için:
print("merhaba\tpython") # merhaba	python
# tab kadar boşluk bırakır. 4 veya 8 boşluk olabilir. 

# \b - backspace karakteri eklemek için:
print("merhaba\bpython") # merhbapython
# backspace karakteri ile bir karakter silinir.
# imleci bir karakter geri alır ve o karakteri siler.

# octal value - \ooo 8lik değer - ASCII tablosundaki karakterlerin 8lik değerlerini kullanabiliriz.
print("\110\145\154\154\157") # Hello

# hex value - \xhh 16lık değer - ASCII tablosundaki karakterlerin 16lık değerlerini kullanabiliriz.
print("\x48\x65\x6c\x6c\x6f") # Hello