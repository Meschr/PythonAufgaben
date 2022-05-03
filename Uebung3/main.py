import Universe

universe = Universe.create(5,5)

for i in range(0,5,1):
    print("Generation " + str(i+1) + ":")
    Universe.display(universe)
    neighbors = Universe.getNeighbors(universe)
    universe = Universe.nextGeneration(universe,neighbors)



