# ex15 - loops - if - driving licence

driverAge = int(input("\nWhat is your age? "))
legalAgeToDrive = 18

if driverAge >= legalAgeToDrive:
    print("\nYou're", (driverAge),"years old. You're allowed to drive.\n")
else:
    yearsInWaiting = legalAgeToDrive - driverAge
    print("\nYou're", (driverAge),"years old. You're NOT allowed to drive for", (yearsInWaiting),"more years.\n")