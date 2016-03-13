#self avoiding random walk of 5000 steps, no border constraints

import random
import statistics

iterations = 10
distances = []
sizes = []
remaining = iterations

while (remaining > 0) :
    steps = 5000
    lattice = []
    contin = True


    #set (0,0) to "visited"
    lattice.append((0,0))

    curx = 0
    cury = 0

    maxx = 0
    maxy = 0
    minx = 0
    miny = 0

    while(contin) :
        moves = []

        #create a list of the available next moves
        #check left
        x = curx - 1
        y = cury
        if (x,y) not in lattice :
            moves.append((x,y))

        #check right
        x = curx + 1
        if (x,y) not in lattice :
            moves.append((x,y))

        #check up
        x = curx
        y = cury + 1
        if (x,y) not in lattice :
            moves.append((x,y))

        #check down
        y = cury - 1
        if (x,y) not in lattice :
            moves.append((x,y))

        if moves == [] :
            contin = False
            print("No available moves")
            
            continue

        if steps == 0 :
            contin = False
            print("No more steps")
            continue

        #choose one move at random
        move = random.choice(moves)

        #update current location
        curx = move[0]
        cury = move[1]

        #mark it as visited
        lattice.append(move)

        #check if it replaces a max or min
        maxx = max(maxx, curx)
        minx = min(minx, curx)
        maxy = max(maxy, cury)
        miny = min(miny, cury)

        steps -= 1
    
    remaining -= 1
    distance = abs(0-curx) + abs(0-cury)
    size = (maxx-minx)*(maxy-miny)
    distances.append(distance)
    sizes.append(size)

    print("Iteration #", (iterations-remaining), "\t : Distance ", distance, ", Lattice size ", size)

#calculations

#averages
distMean = statistics.mean(distances)
sizeMean = statistics.mean(sizes)

#median
distMed = statistics.median(distances)
sizeMed = statistics.median(sizes)

#variance
distVar = statistics.variance(distances)
sizeVar = statistics.variance(sizes)

#standard deviation
distStd = statistics.stdev(distances)
sizeStd = statistics.stdev(sizes)

print("Distance: Mean {:.2f}; Median {:.2f}; Variance {:.2f}; Standard dev {:.2f}" .format(distMean, distMed, distVar,  distStd))
print("Lattice size: Mean {:.2f}; Median {:.2f}; Variance {:.2f}; Standard dev {:.2f}" .format(sizeMean, sizeMed, sizeVar,  sizeStd))




