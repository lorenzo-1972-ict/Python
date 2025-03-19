name = "Lorenzo"
surname = "Emond"
completeName = name +" "+surname
print(completeName)
print("Your complete name has", len(completeName),"characters")
print(str.upper(completeName))
print(str.lower(completeName))
print(completeName, str.endswith(completeName,"nd"))
print(completeName, type(str.endswith(completeName,"nd")))
print(completeName, str.index(completeName,"on"))
print(completeName, str(str.split(completeName," ")))
print(completeName, str(str.strip(completeName,"Emond")))