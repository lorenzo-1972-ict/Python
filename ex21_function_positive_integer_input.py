# script with function asking for a postive integer

def positiveInteger():
    number = input("\nProvide a positive integer: ")
    if type(number) == str:
        number = -1
    while type(number) != int or int(number) < 0:
        number = input("\nEnter a correct value:")
        if type(number) == str:
            number = -1
    print("\nProvided number is correct:", number,"\n")
    
positiveInteger()