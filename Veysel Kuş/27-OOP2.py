
#? Inheritance (Kalıtım/Miras Alma)

class Kisi:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def myPrint(self):
        print(self.firstname, self.lastname)

class Ogrenci(Kisi): #* Kisi class'ını miras alır
    def __init__(self, fname, lname,year): #* kendi constructur'ı
        super().__init__(fname, lname) #* super() kalıtım aldığı sınıfı gösterir
        #! kendi constructur'ını oluşturunca o alana ait kalıtımı kaybeder ve bunu yaparak(super()) kalıtım almaya devam ettirdik
        self.graduationyear = year
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

k1 = Ogrenci("Veysel","KUŞ",2021)
k1.myPrint()
print(k1.graduationyear)

k1.welcome()

#? Metot Ezme
print()

class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Mouse(Animal):
    ...

dog = Dog()
cat = Cat()
mouse = Mouse()
print(dog.speak())
print(cat.speak())
print(mouse.speak())

#?
print()
print(isinstance(dog, Dog)) # dog nesnesi Dog sınıfından mı? True
print(isinstance(dog, Animal)) # dog nesnesi Animal sınıfından mı? True
print(isinstance(dog, Cat)) # dog nesnesi Cat sınıfından mı? False
print(issubclass(Dog, Animal)) # Dog sınıfı Animal sınıfından mı türemiş? True
print(issubclass(Dog, Cat)) # Dog sınıfı Cat sınıfından mı türemiş? False