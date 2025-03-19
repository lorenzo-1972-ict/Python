# script with function performing a countdown

def countdown():
    number = int(input("\nWhat value do you wish to countdown? "))
    while number >= 0:
        if number != 0:
            print(number)
        else:
            print("BOUM!!")                
        number -= 1        
countdown()