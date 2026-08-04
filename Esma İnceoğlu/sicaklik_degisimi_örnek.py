sicaklik=float(input("sıcaklığı giriniz:"))
print("1-celsius-->fahrenheit")
print("2-fahrenheit-->celsius")
secim=input("seçiminizi yapınız:")

if secim=="1":
    sonuc1=(sicaklik*9/5)+32
    print("sıcaklık dönüşüm sonucu:",sonuc1)

elif secim=="2":
    sonuc2=(sicaklik-32)*5/9
    print("sıcaklık dönüşüm sonucu:",sonuc2)

else :
    print("hatalı seçim")    

#print("Sıcaklık dönüşüm sonucu: " + str(sonuc1)) ile dönüştürerek de yapabiliriz
#print(f"Sıcaklık dönüşüm sonucu: {sonuc1}") ile de yapılabilir
    