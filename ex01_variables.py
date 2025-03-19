print("Hello World")

name = 'Lorenzo'
print("Hello", name)

veryLongName = 'Serhat'
print("Hello", veryLongName)

###############################################################################

legalAgeToDrive = 18
lorenzoAge = 52

if (lorenzoAge >= legalAgeToDrive):
    print("\nLorenzo is allowed to drive")
else:
    print("Lorenzo isn't allowed to drive")

if (lorenzoAge >= legalAgeToDrive):
    allowedToDrive = True
else:
    allowedToDrive = False
print("Is Lorenzo allowed to drive?", allowedToDrive)

###############################################################################

score = 20
print(score)

score = "11"
print(score)
print("score is a:", type(score))

###############################################################################

number = 25 + 2.5 +2.5
print(number)
print("number is a:", type(number))

number = int(25 + 2.5 +2.5)
print(number)
print("number is a:", type(number))