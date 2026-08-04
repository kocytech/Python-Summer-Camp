# stringlerde değişim işlemleri yapabiliriz.

text = "python programlama iyi gidiyor"
# büyük harfe çevirme / upper() metodu
print(text.upper()) # PYTHON PROGRAMLAMA İYİ GİDİYOR

# küçük harfe çevirme / lower() metodu
print(text.lower()) # python programlama iyi gidiyor    

# baştan ve sondan boşlukları silme / strip() metodu
text2 = "   python programlama iyi gidiyor   "  
print(text2.strip()) # python programlama iyi gidiyor

# yer değiştirme / replace() metodu 
# bir şeyin yerine başka bir şey koymak için kullanılır.
print(text.replace("iyi", "çok berbat")) # python programlama çok berbat gidiyor  

# stringlerde bölme / split() metodu
# bir stringi belirli bir karaktere göre böler ve liste olarak döndürür.
programlama_dilleri = "python, java, c#, c++, php"
print(programlama_dilleri.split(",")) # ['python', ' java', ' c#', ' c++', ' php'] şeklinde liste döndürür. 



