from collections import defaultdict
import numpy

GRID_ROWS = 8
GRID_COLS = 12

UNUSED = "UNUSED"
NAN = "NAN"

def main():
    filepath = input("Please provide the file to solve for: ")
    file = ReadFile(filepath)
    manifest = ParseFile(file)
    startGrid = CreateGrid(manifest)

class Container:
    def __init__(self, coord, weight, item):
        self.coord = coord
        self.weight = weight
        self.item = item

class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def MoveToColumn(grid:numpy.ndarray, container:Container, newColumn:int):
    # TODO: create a copy of the grid aka node
    
    # find the highest empty space in the new column
    for i in range(GRID_ROWS):
        check:Container = grid[i][newColumn]
        if check.item == UNUSED:
            emptySpace = check
            break

    # calculate cost of swap
    costSwap = CostSwap(grid, container.coord.col, newColumn)

    # swap empty and containers positions above it
    emptyCoord = emptySpace.coord
    currCoord = container.coord
    grid[currCoord.row][currCoord.col] = emptySpace
    grid[emptyCoord.row][emptyCoord.col] = container

    return costSwap

# returns the amount the crane needs to move to get from col1 to col2
def CostSwap(grid, col1, col2):
    raise NotImplementedError("need to implement this!")

def Height(grid:numpy.ndarray, column):
    height = 0
    for i in range(GRID_ROWS):
        container:Container = grid[i][column]
        if (container.item == UNUSED): # empty space, no items above it
            return height
        elif (container.item != NAN):  # non-empty, non-null space
            height += 1
    return height

def CheckBalance(grid:numpy.ndarray):
    # Case 1: difference less than limit
    # sum the left and right halves
    sumLeft = 0
    sumRight = 0
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS / 2):
            leftItem = grid[i][j]
            rightItem = grid[i][GRID_COLS / 2 + j]
            sumLeft += leftItem[1]
            sumRight += rightItem[1]

    difference = abs(sumLeft - sumRight)
    limit = sumLeft + sumRight * 0.10

    return difference < limit or difference == 0

    # TODO: Case 2: difference is minimal

def CreateGrid(manifest):
    grid = numpy.zeros((GRID_ROWS, GRID_COLS), dtype=Container)
    for i in range(len(manifest)):
        coord:Coordinate = manifest[i].coord
        grid[coord.row - 1, coord.col - 1] = manifest[i]
    return grid

# returns array of strings read from filename
def ReadFile(filename):
    file = open(filename, mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    file.close()
    return lines

# creates data representation of manifest
def ParseFile(lines):
    manifest = []
    for line in lines:
        # get plain text [01, 01], {00000}, NAN
        parts = line.split(", ")
        # get int representation of the coordinate [1,1]
        x, y = parts[0].strip("[]").split(",")
        coord = Coordinate(int(x), int(y))
        # get the id "{00000}"
        weight = int(parts[1].strip("{}"))
        # get the item "NAN"
        item = parts[2].strip("\n")

        container = Container(coord, weight, item)
        manifest.append(container)
    return manifest

if __name__ == "__main__":
    main()