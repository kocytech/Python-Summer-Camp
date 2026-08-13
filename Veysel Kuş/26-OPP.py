
# class Vehicle:
#     brand = "Skoda" #* property 
#     model = "Superb" #* property 
#     color = "White" #* property 
#     def __init__(self): #* constructor method , ilk burası çalışır ve yazmasanız da her zaman vardır
#         ...

# car_obj = Vehicle()
# print("Brand =",car_obj.brand)
# print("Model =",car_obj.model)
# print("Color =",car_obj.color)


class Vehicle:
    def __init__(self,brand,model,color):
        self.brand = brand 
        self.model = model
        self.color = color
        #* atama için constructor methodunun ilk parametresi kullanılır

car1_obj = Vehicle("Skoda","Superb","White")
car2_obj = Vehicle("Honda","Civic","Green")
car3_obj = Vehicle("Nissan","Juke","Black")

print(f"{car1_obj.brand}, {car1_obj.model}, {car1_obj.color}")
print(f"{car2_obj.brand}, {car2_obj.model}, {car2_obj.color}")
print(f"{car3_obj.brand}, {car3_obj.model}, {car3_obj.color}")


print()

class Person:
    def __init__(self,n,a): 
        self.name = n
        self.age = a
    def __str__(self): #* kullanıcının göreceği bir dunder(magic) method, fronted gibi önyüzde görülecek şeyler buraya yazılır
        return f"Name: {self.name}\nAge: {self.age}"
    def __repr__(self): #* yazılım geliştiricilerib göreceği bir dunder(magic) method, hata ayıklama veya değişkenleri/değerleri daha detaylı görebilmek için kullanılır 
        return f"Name: {self.name!r}\nAge: {self.age!r}"

p1 = Person("Veysel",19)
print(p1)
print(repr(p1)) #* str methodu return ediyor bu yüzden repr methoduna girmiyor girmesi için böyle çağırıyoruz

print()
class Person2:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def myInfo(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age} years old")

prsn1 = Person2("Veysel",18)
prsn1.myInfo()

#* Bir sınıfın içindeki Dunder(magic) methodları kendiliğinden çalışırken kendimiz oluşturduğumuz methodları .method_adı() ile çağırmamız gerekir
