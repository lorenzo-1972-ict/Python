# script to illustrate try & catch
 
try:
    res = 10 / 0

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    print("The result is:", result)

finally:
    print("This will always execute.")