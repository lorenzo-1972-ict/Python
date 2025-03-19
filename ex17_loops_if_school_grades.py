# script to provide letter grades corresponding to %

studentGrade = int(input("\nWhat's the achieved grade in %? "))

if 90 <= studentGrade <= 100:
    print("\nThe grade letter is S.\n")

elif 80 <= studentGrade <= 89:
    print("\nThe grade letter is A.\n")

elif 70 <= studentGrade <= 79:
    print("\nThe grade letter is B.\n")

elif 60 <= studentGrade <= 69:
    print("\nThe grade letter is C.\n")

elif 50 <= studentGrade <= 59:
    print("\nThe grade letter is D.\n")

elif 40 <= studentGrade <= 49:
    print("\nThe grade letter is E.\n")

else:
    print("\nThe grade letter is F.\n")