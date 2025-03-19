# script to compute the weekly salary

workedHoursPerWeek = input("\nHow many hours per week do you work (hrs)? ")
hourlyRate = input("\nWhat is your hourly rate (€/h)? ")
weekSalary = int(workedHoursPerWeek) * int(hourlyRate)
print("\nYour weekly salary is:", weekSalary, "€")