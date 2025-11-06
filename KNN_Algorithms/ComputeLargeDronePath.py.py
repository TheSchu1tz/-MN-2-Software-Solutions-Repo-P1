import math
import random

#MO: Helper assigns a number of nodes to classify for each cluster center in a list
def assign_num_nodes(num_nodes: int, num_centers: int):
    #Calculate how many nodes each center will classify
    nodes_per_center = num_nodes // num_centers
    remainder_nodes = num_nodes % num_centers

    assigned_nodes = [nodes_per_center] * num_centers

    if remainder_nodes != 0: #Case if we cannot evenly distribute nodes
        i = 0
        while i < remainder_nodes :
            assigned_nodes[i % num_centers] += 1
            i += 1
    
    return assigned_nodes

def classify_nodes(cluster_centers: list, all_coordinates: list):

    coord_indices = [i for i in range(len(all_coordinates))]
    current_center = 0
    while current_center < len(cluster_centers)

def KNN_Classify(all_coordinates: list, num_centers: int):

    nodes_per_cluster_list = assign_num_nodes(len(all_coordinates), num_centers)

    #Start with random darts
    cluster_centers = [(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(num_centers)] 
    #Initialize center coordinates on the map
    #Find KNN for each center
    #Reestimate centers
    #Keep going until centers stop changing
    return

if __name__== "__main__":
    #TESTS
    test_nodes = [i for i in range(15)]
    for i in range(1,5):
        assign_num_nodes(len(test_nodes), i)
