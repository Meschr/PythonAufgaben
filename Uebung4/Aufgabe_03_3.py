from Aufgabe_03_2 import Universe

rows = int(input("Enter number of rows of the universe: "))
cols = int(input("Enter number of cols of the universe: "))
iterations = int(input("Enter number of iterations for the universe: "))

universe = Universe(rows, cols)
universe.display()

for i in range(0, iterations):
    print("\n---------------Iteration: " + str(i) + " -----------------")
    universe.nextGeneration()
    universe.display()
