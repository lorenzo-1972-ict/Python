# script to provide letter grades corresponding to %

studentGrade = int(input("\nWhat's the achieved grade in %? "))
gradesTable = {
    "S": (90,100),
    "A": (80,89),
    "B": (70,79),
    "C": (60,69),
    "D": (50,59),
    "E": (40,49),
    "F": (0,39)}

for line in gradesTable.items():
    if line[1][0] < studentGrade < line[1][1]:
        print("\nThe grade letter is", line[0], ".\n")