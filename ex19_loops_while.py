# scripts

############################################################################################

counter = 0
while counter <= 5:
    print(counter)
    counter +=1

else: 
    print(f"End of app. Counter value:", counter)

############################################################################################

# loop without matching the condition > infinite loop

counter = 0
while counter < 5:
    print(counter)
    
else: 
    print(f"End of app. Counter value:", counter)

############################################################################################

answer = input("Hello, fill in your grade")
print(answer, type(reponse))

while type(answer) != type(int):
    answer = input("Enter a correct value")
    print(answer, type(reponse), type(int))

else:
    print("End app")


############################################################################################

nombres = (0,1,2,3,4,5)

for nombre in nombres:
    print(nombre)
    if nombre == 3:
        break

for nombre in nombres:
    print(nombre)
    if nombre == 3:
        continue
    print    

else:
    print("End of loop")
