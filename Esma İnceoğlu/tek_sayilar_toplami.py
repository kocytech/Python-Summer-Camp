sayi=int(input("bir sayi giriniz:"))
toplam=0

for x in range(sayi):
    if  x % 2 !=0 :
        toplam=toplam+x

print(toplam)        