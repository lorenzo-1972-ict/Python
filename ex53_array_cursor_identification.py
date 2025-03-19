# script to illustrate cursor move within an array

array = [   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

cursorPositions = []

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 1 :
            cursorX = i+1
            cursorY = j+1
            cursorPositions.append((cursorX,cursorY))

print("\nCursors positions in array: ",cursorPositions,"\n")