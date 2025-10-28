import random
import math
import time
import os
import threading
import numpy

#MO: Using nudri001's function
def CreateDistanceMatrix(coords):
    distMatrix = numpy.empty((len(coords), len(coords)))
    for x, coord1 in enumerate(coords):
        for y, coord2 in enumerate(coords):
            distance = math.dist(coord1, coord2)
            distMatrix[x,y] = distance
    return distMatrix

#MO: Need this to end execution on enter keystroke
stop = False
def wait_for_key():
    global stop
    input()
    stop = True

#MO: This is a basic search that searching random permutations of the path to find the optimal one
def dumb_search(coordinates: list):

    best_solution = float("inf")
    best_path = coordinates.copy()

    start = time.time() #MO: This is to time the search

    threading.Thread(target=wait_for_key, daemon=True).start()
   
    while(not stop):
        curr_solution = 0
        trees_coords = coordinates[1:]
        random.shuffle(trees_coords)
        curr_path = [coordinates[0]] + trees_coords + [coordinates[0]]
        for i in range(len(curr_path) - 1):
            left = curr_path[i]
            right = curr_path[i+1]
            curr_solution += math.dist(left, right)
        
        if curr_solution < best_solution:
            end = time.time()
            print(f"\t\t{curr_solution}m found at {round(end - start, 2)}s")
            best_solution = curr_solution
            best_path = curr_path.copy()
    
    return best_solution, best_path

#MO: This is a modified basic search that incorporates pruning whenever a distance 
#MO: found is greater than the current best solution
def prune_search(coordinates: list):

    best_solution = float("inf")
    #best_path = coordinates.copy()
    best_path = []
    coord_indexes = [i for i in range(len(coordinates))]

    pruned = False

    start = time.time() #MO: This is to time the search

    threading.Thread(target=wait_for_key, daemon=True).start()
    
    while(not stop):
        curr_solution = 0.0
        trees_coords = coord_indexes[1:].copy()
        random.shuffle(trees_coords)
        curr_path = [0] + trees_coords + [0]
        pruned = False

        for i in range(len(curr_path) - 1):
            left = coordinates[curr_path[i]]
            right = coordinates[curr_path[i+1]]
            curr_solution += math.dist(left, right)
            if curr_solution >= best_solution:
                pruned = True
                break
        
        if curr_solution < best_solution and not pruned:
            end = time.time()
            print(f"\t\t{curr_solution}m found at {round(end - start, 2)}s")
            best_solution = curr_solution
            best_path = curr_path.copy()
        
    return best_solution, best_path

#MO: This function computes the nearest neighbor path. 
##   If randomize is True, it will do a nearest neighbor with a random chance of deviation.
def compute_NN(coord_indexes:list, coordinates:list, randomize:bool):
    nn_path = [0]
    visited = set()
    visited.add(0)
    nn_solution = 0

    current_index = 0

    for _ in range(len(coord_indexes)):
        first_closest_index = None
        first_closest_dist = float('inf')
        second_closest_index = None
        second_closest_dist = float('inf')
        for j in coord_indexes:

            if j not in visited and j != current_index:
                left = coordinates[current_index]
                right = coordinates[j]
                left_right_dist = math.dist(left, right)

                if left_right_dist < first_closest_dist:
                    second_closest_dist = first_closest_dist
                    second_closest_index = first_closest_index
                    first_closest_index = j
                    first_closest_dist = left_right_dist
                elif left_right_dist < second_closest_dist:
                    second_closest_dist = left_right_dist
                    second_closest_index = j
                    
        if first_closest_index is None:
            break
        if randomize and second_closest_index is not None and random.random() < 0.1:
            closest_index = second_closest_index
            closest_distance = second_closest_dist
        else:
            closest_index = first_closest_index
            closest_distance = first_closest_dist

        visited.add(closest_index)
        nn_path.append(closest_index)
        nn_solution += closest_distance
        current_index = closest_index
    
    nn_solution += math.dist(coordinates[0], coordinates[current_index])
    nn_path.append(0)
    return nn_path, nn_solution

#MO: This function performs a nearest neighbor search with random path variation
def NN_random_search(coordinates: list):

    best_solution = float("inf")
    best_path = []
    coord_indexes = [i for i in range(len(coordinates))]

    start = time.time() #MO: This is to time the search

    threading.Thread(target=wait_for_key, daemon=True).start()

    #MO: Compute NN path
    nn_path, nn_solution = compute_NN(coord_indexes, coordinates, False)
    #MO: Set our baseline as the nn_solution and begin modified search
    best_path = nn_path.copy()
    best_solution = nn_solution 

    end = time.time()
    print(f"\t\t{best_solution}m found at {round(end - start, 2)}s")

    random_path = []
    random_solution = float('inf')
    while (not stop):
        coord_indexes = [i for i in range(len(coordinates))]
        random_path, random_solution = compute_NN(coord_indexes, coordinates, True)
        if random_solution <= best_solution:
            end = time.time()
            print(f"\t\t{random_solution}m found at {round(end - start, 2)}s")
            best_solution = random_solution
            best_path = random_path

    return best_solution, best_path



if __name__=="__main__":

    filename = input("Enter the name of file: ")

    coordinates = []

    with open(filename, 'r') as file:
        for line in file:
            x, y = tuple(map(float, line.split()))
            coordinates.append((x,y))
    
    print(f"There are {len(coordinates)} nodes, calculating route..\n\tShortest Route Discovered So Far")
    #best_solution, best_path = dumb_search(coordinates)
    #best_solution, best_path = prune_search(coordinates)
    best_solution, best_path = NN_random_search(coordinates)
    solution_filename = "test_solutions/" + os.path.basename(filename) + "_solution_" + str(best_solution) + ".txt"

    with open(solution_filename, 'w') as f:
        for index in best_path:
            f.write(str(index) + "\n")

    print(f"Route written to disk as test_solutions/{os.path.basename(filename)}_solution_{best_solution}.txt")
    
    
            
    
    