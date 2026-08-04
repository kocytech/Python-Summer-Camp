import math

#? Sabitler
print("-----Sabitler-----")
print("math.e =>",math.e)
print("math.inf =>",math.inf)
print("-math.inf =>",-math.inf)
print("math.nan =>",math.nan)
print("math.pi =>",math.pi)
print("math.tau =>",math.tau)

#? Açılar
print("-----Açılar-----")
print("math.acos(0.55) =>",math.acos(0.55))
print("math.acosh(7) =>",math.acosh(7))
print("math.asin(0.55 =>",math.asin(0.55))
print("math.asinh(7) =>",math.asinh(7))
print("math.atan(0.4) =>",math.atan(0.4))
print("math.atan2(8,5) =>",math.atan2(8,5))
print("math.atanh(0.59) =>",math.atanh(0.59))
print("math.cos(0) =>",math.cos(0))
print("math.cosh(1) =>",math.cosh(1))
print("math.sin(0) =>",math.sin(0))
print("math.sinh(0) =>",math.sinh(0))

#?
print()
print("math.degrees(8.9) =>",math.degrees(8.9)) #* radyanı dereceye çevirir
print("math.radians(180) =>",math.radians(180)) #* dereceyi radyana çevirir

#? 
print()
print("math.ceil(1.1) =>",math.ceil(1.1)) #* bi üst tam sayıya yuvarlar
print("math.floor(1.9) =>",math.floor(1.9)) #* bi alt tam sayıya yuvarlar
print("math.sqrt(10) =>",math.sqrt(10)) #* karakökü alır
print("math.isqrt(10) =>",math.isqrt(10)) #* karakökü alır ama int, yani sqrt + floor gibi
print("math.trunc(45.7438057) =>",math.trunc(45.7438057)) #* ondalıklı kısmını atar
print("math.remainder(19,4) =>",math.remainder(19,4)) #* 1.parametrenin 2.parametreye bölümünü verir
#* dönen_değer = 1.parametre - (bölümün yüksek en yakın tam sayısı(ceil) * 2.parametre)

#?
print()
print("math.comb(7,4) =>",math.comb(7,4)) #* kombinasyon alır
print("math.copysign(7,-19) =>",math.copysign(7,-19)) #* 1.parametrenin değerini 2.parametrenin işaretini alır 
p = [3,3]
q = [6,7]
print("math.dist(p,q) =>",math.dist(p,q)) #* 2 nokta arası mesafeyi hesaplar
print("math.erf(0.7) =>",math.erf(0.7))
print("math.erfc(0.7) =>",math.erfc(0.7))
#* erf(x) + erfc(x) = 1
print("math.exp(1) =>",math.exp(1)) #* e üzeri 1.parametre(1) 
print("math.expm1(1) =>",math.expm1(1)) #* e üzeri 1.parametre(1) 
#* exp() ve expm1() arsındaki fark expm1() hassas ölçümler için daha iyidir
print("math.exp2(1) =>",math.exp2(1)) #* 2 üzeri 1.parametre(1)
