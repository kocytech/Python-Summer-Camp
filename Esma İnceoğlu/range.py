#range() Python'da döngülerle en çok kullanılan fonksiyonlardan biridir.
#qiskit de de çok kullanacağımız fonksiyonlardandr
#range() belirli bir sayı aralığı oluşturur. 
#Genellikle for döngüsüyle birlikte kullanılır.
for i in range(5):
    print(i)

#range(5) 5'e kadar değil, 5 hariç sayıları üretir.
#Başlangıç: 0 , Bitiş: 5 dahil değil

#range(başlangıç,bitiş) bitiş dahil değil!!
for i in range(2, 7):
    print(i)

#range(başlangıç,bitiş,adım)  adım + ise ileri - ise geri sayar
# 
# 
# range() ile liste oluşturma 
sayilar = list(range(5))
print(sayilar)   

#Qiskit de neden önemli 
#örneğin 5 kübite h kapısı uygulamak istersek:
#for i in range(5):
 #   qc.h(i)

#Bu döngü şu işlemleri yapar:
#qc.h(0)
#qc.h(1)
#qc.h(2)
#qc.h(3)
#qc.h(4)
#Yani tek tek yazmana gerek kalmaz.    

