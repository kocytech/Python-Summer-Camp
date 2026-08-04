# şart ifadeleri.
# şu olursa şunu yap bu olursa bunu yap gibi komutlar vermek için kullanırız.
# if ile yazarız
# köşeli parantez yok iki nokta var :
# sonrasında girinti çıkıntılar ile

if 70 > 7:
    print("True")

# koşulun gerçekleşmediği durumlar için elif = başka demek

if 7 > 7:
    print("True")
elif 7 == 7: # tek eşittir atama çift eşittir sorgulama denklik operatörüdür.
    print("eşit")

# hiç bir koşul gerçekleşmezse else çalışır.

if 7 < 4:
    print("True")
elif 7 == 4: # tek eşittir atama çift eşittir sorgulama denklik operatörüdür.
    print("eşit")
else:
    print("küçük")