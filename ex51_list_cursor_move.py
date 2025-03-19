# script to illustrate cursor move within a

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("List: ", list, "\n")
index = 0

while (1):
    cursor = int(input("Insert cursor move :"))
    list[index] = 0
    list[index + cursor] = 1
    print("\n", list)
    index = index + cursor 
    if (cursor == 0):
        break