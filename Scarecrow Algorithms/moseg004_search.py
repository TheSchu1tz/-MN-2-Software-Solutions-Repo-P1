import random
import math

def dumb_search(coordinates: list):

    best_solution = float("inf")
    best_path = coordinates

    try:
        while(True):
            curr_solution = 0
            trees_coords = coordinates[1:-1]
            random.shuffle(trees_coords)
            coordinates[1:-1] = trees_coords
            for i in range(len(coordinates) - 1):
                left = coordinates[i]
                right = coordinates[i+1]
                curr_solution += math.dist(left, right)
            
            if curr_solution < best_solution:
                print(f"\t\t{curr_solution}")
                best_solution = curr_solution
                best_path = coordinates
    except:
        KeyboardInterrupt
        return best_solution, best_path

if __name__=="__main__":

    filename = input("Enter the name of file: ")

    coordinates = []

    with open(filename, 'r') as file:
        for line in file:
            x, y = tuple(map(int, line.split()))
            coordinates.append((x,y))
    
    print(f"There are {len(coordinates)} nodes, calculating route..\n\tShortest Route Discovered So Far")
    best_solution, best_path = dumb_search(coordinates)
    solution_filename = filename + "_solution_" + str(best_solution) + ".txt"

    with open(solution_filename, 'w') as f:
        for x,y in best_path:
            f.write(str(x) + " " + str(y) + "\n")

    print(f"Route written to disk as {filename}_solution_{best_solution}.txt")
    
    
            
    
    