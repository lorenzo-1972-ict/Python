# ex16 - loops - if - age difference

ageLorenzo = 52
ageFriend = int(input("\nWhat is your age my friend? "))
ageDifference = ageLorenzo - ageFriend

if -1 <= ageDifference <= 1:
    print("\nWe're less than 1 year old apart.\n")

elif ageDifference > 0:
    print("\nYou're", (ageDifference),"younger than me.\n")

else:
    print("\nYou're", abs(ageDifference),"older than me.\n")