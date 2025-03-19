# scripts to manipulate strings

desertTastes = "Chocolate Vanilla Strawberry" 
pizzaTastes = "Cheese Pizza"
fruits = "Apple, Pear, Banana, Orange, Sherry, Mango, Pineapple"

#3
print(desertTastes)

#4
print(len(desertTastes))

#5
print(str.upper(desertTastes))

#6
print(str.lower(desertTastes))

#7.1
print(str.capitalize(desertTastes))

#7.2 
print(str.title(desertTastes))

#7.3
print(str.swapcase(desertTastes))

#8
print(desertTastes[0:8])

#9
choice = desertTastes.find("Vanilla")
print("Vanilla available?",bool(choice))

#10
newChoice = "Caramel"
newListTastes = desertTastes.replace ("Chocolate", newChoice)
print(newListTastes)

#11
print (pizzaTastes.replace ("Cheese Pizza", "Mushrooms Pizza"))

#12
print(str.split(desertTastes, " "))

#13
print(str.split(fruits, ","))

#14
print(desertTastes[0])

#15

#16


