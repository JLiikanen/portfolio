'''
Acceptable params to the function are two-dimensional matrices (arrays) such as 

[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

''' 


def riverSizes(matrix):
    ylimits = (0, len(matrix) - 1)
    xlimits = (0, len(matrix[0]) - 1)
    rivers = []



    def radarRight(xPos : int, ypos : int) -> int: # recursive radar search function
        count = 0
        newPos = xPos + 1
        if (newPos == xlimits[1] and matrix[ypos][newPos] == 1):  #basecase we reach a border
            matrix[ypos][newPos] = 2  # changing the counted rivers to two to signify counted rivers
            count += 1
            return count + radarUp(newPos, ypos) + radarDown(newPos, ypos)         # call radarUp and down as L shape form is possible
        elif (newPos >= xlimits[1]):
            return count
        else:
            if (matrix[ypos][newPos] == 1):
                matrix[ypos][newPos] = 2
                count +=1
                return count + radarRight(newPos, ypos) + radarUp(newPos, ypos) + radarDown(newPos, ypos)
            else:
                return count

    def radarLeft(xPos: int, ypos : int):
        count = 0
        newPos = xPos - 1
        if (newPos == 0 and matrix[ypos][newPos] == 1):  # basecase we reach a border, mitä jos menee yli?
            count += 1
            matrix[ypos][newPos] = 2
            return count + radarUp(newPos, ypos) + radarDown(newPos, ypos)  # syötä argumenttina uusi sijainti
        elif (newPos <= 0):
            return count
        else:
            if (matrix[ypos][newPos] == 1):
                count += 1
                matrix[ypos][newPos] = 2
                return count + radarLeft(newPos, ypos) + radarUp(newPos, ypos) + radarDown(newPos, ypos)
            else:
                return count

    def radarUp(xPos: int, ypos : int):
        count = 0
        newPos = ypos - 1
        if (newPos == 0 and matrix[newPos][xPos] == 1):  # basecase we reach a border
            count += 1
            matrix[newPos][xPos] = 2
            return count + radarRight(xPos, newPos) + radarLeft(xPos, newPos) # radars to left and right
        elif (newPos <= 0):  # turhaa koodia
            return count
        else:
            if (matrix[newPos][xPos] == 1):
                count += 1
                matrix[newPos][xPos] = 2
                return count + radarUp(xPos, newPos) + radarRight(xPos, newPos) + radarLeft(xPos, newPos)
            else:
                return count

    def radarDown(xPos: int, ypos: int):  # palautuu liian aikasin
        count = 0
        newYpos = ypos + 1           # jos ehto ei toteutdu
        if (newYpos == ylimits[1] and matrix[newYpos][xPos] == 1):  # basecase we reach a border and we are on a one position
            #print("bordercase")
            matrix[newYpos][xPos] = 2
            count += 1
            return (count + radarRight(xPos, newYpos) + radarLeft(xPos, newYpos)) # radars to left and right
        elif (newYpos >= ylimits[1]):  # otettava huomiion myös jos newpos on nolla, sillä jo ylempi ehto sitten kertoo sen että matrix[newPos][xPos] == 1 anto falsea
            return count
        else:
            if (matrix[newYpos][xPos] == 1):
                count += 1
                matrix[newYpos][xPos] = 2
                return count + radarDown(xPos, newYpos) + radarRight(xPos, newYpos) + radarLeft(xPos, newYpos)
            else:
                return count

    y = -1
    for row in matrix: 
        x = -1
        y += 1
        for pos in row:
            x += 1
            if pos == 1:
                matrix[y][x] = 2
                riverlen = radarRight(x, y) + radarLeft(x, y) + radarUp(x, y) + radarDown(x, y) + 1  
                rivers.append(riverlen)

    return rivers
