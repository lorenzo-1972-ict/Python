name = "Lorenzo"
age = 52

print ("\nHello {}, you are {}.".format(name, age))

print (f"\nHello {name}, you are {age}.")

##########################################################################################

# replace
# title
# swapcase

print (str.swapcase("\nHello\n"))
print ("\nHello" [:: -1])

phrase = "Hello, how are you doing? \n" "Very well for myself\n"
print(phrase)

##########################################################################################

#isalpha()
print(str.isalpha("Hello"))
print(str.isalpha("Hello "))

#isdecimal()
print(type(str.isalpha("123abc")))
print(type(str.isalpha("123abc ")))

#isdigit() // isnumeric()
print(str.isdigit("1234567890"))
print(str.isnumeric("1234567890"))
print(str.isnumeric("123+456"))

#isupper // 