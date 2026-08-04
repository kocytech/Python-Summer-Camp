"""
for degisken in dizi:
"""
#! foreach mantığı


fruits = ["Graphe","Orange","Strawberry","Pineapple","Melon","Matermelon"]

for fruit in fruits:
    print(fruit)
    if(fruit=="Orange"):
        continue
    if(fruit=="Strawberry"):
        break

for number in range(8): #* range(8): 0(dahil)'dan 8(dahil değil)'e sayı listesi oluşturur
    print(number,end=" ") #* end="": sonuna ne yazılacağı

for i in range(3):
    ... #* henüz doldurmadığımızda sonra doldurmak istediğimizde ... ya da pass kullanılır