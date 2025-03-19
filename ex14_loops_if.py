# scripts to illustrate loops.. condistions.. if..

################################################################################################

# if #1
a = 3
if a > 0:
    print ("1/ A is a positive number")

# if #2
a = -3
if a < 0:
    a = 5
    print ("2/ A is a positive number")

# if #3
a = None
if a:
    a = 5
    print ("3/ A is a positive number")

# if #4
a = "Hello"
if a:
    a = 5
    print ("4/ A is a positive number")

# if #5
a = 3
if a > 0:
    print ("5/ A is a positive number")
else:
    print ("5/ A is a negative number")
    
# if #6
a = -3
if a > 0:
    print ("6/ A is a positive number")

elif a < 0:
    print ("6/ A is a negative number")

else :
    print ("6/ A is equal to 0")


# if #7
a = 0
if a > 0 and a % 2 == 0:
    print ("7/ A is a positive integer number")

elif a < 0 and a % 2 == 0:
    print ("7/ A is a negative integer number")

else :
    print ("7/ A is equal to 0")

################################################################################################

# if #8
a = False
b = 0
if a is b:
    print("8/ a = b")
else:
    print("8/ a != b")

################################################################################################

# if #9
user = "admin"
acces_level = 3
if user == "admin" and acces_level >= 3:
    print("9/ Accès autorisé")
else:
    print("9/ Accès refusé")