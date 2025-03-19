# script to illustrate cursor move within an array

array = [   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for line in array:
    print(line)

indexX = 0
indexY = 0

while (1):
    cursorX = int(input("Insert X cursor move :"))
    cursorY = int(input("Insert Y cursor move :"))

    array[indexY + cursorY][indexX + cursorX] = 1
    array[indexY][indexX] = 0
    indexX = indexX + cursorX
    indexY = indexY + cursorY
    
    for line in array:
        print(line)
        
    if (cursorX == 0 and cursorY == 0 ):
        break