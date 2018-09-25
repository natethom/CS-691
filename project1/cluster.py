from random import randint
import copy
import numpy as np

## K-Means
X = np.array([[1,0],[7,4],[9,6],[2,1],[4,8],[0,3],[13,5],[6,8],[7,3],[3,6],
            [2,1],[8,3],[10,2],[3,5],[5,1],[1,9],[10,3],[4,1],[6,6],[2,2]])

rand_data = []
for index in range(0, 100):
    rand_data.append([randint(0, 20), randint(0, 20)])

def K_Means(X,K):
    cluster_centers = []
    cluster_data = []
    max_point = 0
    min_point = 0
    convergence_flag = False

    #find the max and min coordinates in the dataset
    for point in range(0, len(X)):
        for dimension in range(0, len(X[0])):
            if X[point][dimension] > max_point:
                max_point = X[point][dimension]
            if X[point][dimension] < min_point:
                min_point = X[point][dimension]

    #generate random clusters based on max and min values
    for cluster_center in range(0, K):
        cluster_centers.append([randint(min_point, max_point),randint(min_point, max_point)])
        cluster_data.append([])

    #compute distance from points to all cluster centers
    previous_centers = []

    while previous_centers != cluster_centers:
        #check if convergence has been reached
        previous_centers = copy.deepcopy(cluster_centers)

        #iterate through all data points
        for point in X:
            #set the closest cluster to be cluster 0
            closest_cluster = 0
            #The current distance to the closest cluster
            distance_to_closest_cluster = 99999999
            for cluster_center in range(0, K):
                #set a temporary variable to keep track of
                ## distance to cluster_K
                temp_distance_to_closest_cluster = 0
                for dimension in range(0, len(X[0])):
                    temp_distance_to_closest_cluster = (
                    temp_distance_to_closest_cluster + (
                    (point[dimension]-(cluster_centers[cluster_center][dimension]))**2))

                if temp_distance_to_closest_cluster < distance_to_closest_cluster:
                    closest_cluster = cluster_center
                    distance_to_closest_cluster = temp_distance_to_closest_cluster

            cluster_data[closest_cluster].append(point)

        for cluster_center in range(0,K):
            for dimension in range(0,len(X[0])):
                dimension_avg = 0
                for point in cluster_data[cluster_center]:
                    dimension_avg = dimension_avg + point[dimension]
                if dimension_avg != 0:
                    dimension_avg = dimension_avg / len(cluster_data[cluster_center])
                    cluster_centers[cluster_center][dimension] = dimension_avg
            cluster_data[cluster_center].clear()

    return np.array(cluster_centers)

def K_Means_better(X, K):
    k_means_return_values = {}
    while True:
        return_value = K_Means(X, K)
        if str(return_value) in k_means_return_values.values():
            print("\nIN IF STATEMENT\n")
            k_means_return_values[str(return_value)]['num_returned'] = k_means_return_values[str(return_value)]['num_returned'] + 1
            return "made it"
        else:
            print("\nIN ELSE STATEMENT\n")
            k_means_return_values[str(return_value)] = {str(return_value):return_value, 'num_returned':1}
        print(f'Dict: \n{k_means_return_values}\n\n')
        print(f'Return Value: \n{return_value}\n\n')
        print(f'Return Value as str: \n{str(return_value)}\n\n')

K_Means_better(X, 2)
#print(f"OUTPUT: {K_Means(X, 5)}")
