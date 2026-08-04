# string bir dizidir.
# diziler 0. indexten başlar.

text = "python programlama dili"
print(text[1:5]) # 1. indexten 5. indexe kadar olan karakterleri verir. 
# 5. index dahil değildir.

# başlangıç inde"xini belirtmezsek 0. indexten başlar.
print(text[:5]) # 0. indexten 5. indexe kadar olan karakterleri verir.
# ilki dahil, ikincisi dahil değildir.

# son inde"xini belirtmezsek son indexe kadar gider.
print(text[5:]) # 5. indexten son indexe kadar olan karakterleri verir.

# -li parametreler ile de dilimleme yapabiliriz.
print(text[-5:-1]) # -5. indexten -1. indexe kadar olan karakterleri verir.

# yine başlangıç dahil , son index dahil değildir.

# stirngi birleştirme işlemi yapabiliriz.
# string concatenation işlemi 

text2 = "python"
text3 = "programlama"
text_toplam = text2 + " " + text3
print(text_toplam) # python programlama şeklinde birleştir
print(text2 + " " + text3) # python programlama şeklinde birleştir

# plus ile birleştirirken araya boşluk koymak istiyorsak bunu kendimiz eklemeliyiz.