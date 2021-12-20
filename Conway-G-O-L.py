# Conway's Game Of Life

import random, time, copy
WIDTH = 60
HEIGHT = 20
 #Creat list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = []    # Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
        #if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            column.append('#') # Adding a living cells
        else:
            column.append('') # Adding dead cells
    nextCells.append(column)    # nextCell is a list of column list
while True:     # Main Game Loop
    print('\n\n\n\n\n') # separating each step with newline
    currentCells = copy.deepcopy(nextCells)
    # Print current cells of screen
    for y in range (HEIGHT):
        for x in range (WIDTH):
            print(currentCells[x][y], end='')       # Printing either # or space
        print()    # Print newline at the end of the row
    # Calculate the next step's cell based on current step's cell
    for x in range(WIDTH):
        for y in range(HEIGHT):
    # Get neighboring coordinate
    # % WIDTH ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
# Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top:left neighbors is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbors is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top:right neighbors is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbors is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbors is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom:left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 #
# Set cells based on conway's rule of life
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
    # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells == '' and numNeighbors == 3:
    # Dead cells with 3 neighbors becomes alive
                nextCells[x][y] = '#'
            else:
    # Everything dies or stay dead:
                nextCells[x][y] = ''
    time.sleep(1) # To reduce flickeri