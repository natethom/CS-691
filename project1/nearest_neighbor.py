import numpy as np

X_train = np.array([[1,5],[2,6],[2,7],[3,7],[3,8],[4,8],[5,1],
                    [5,9],[6,2],[7,2],[7,3],[8,3],[8,4],[9,5]])
Y_train = np.array([[-1],[-1],[1],[-1],[1],[-1],[1],
                    [-1],[1],[-1],[1],[-1],[1],[1]])

X_test = np.array([[1,1], [2,1], [0,10], [10,10], [5,5],
                   [3,10], [9,4], [6,2], [2,2], [8,7]])
Y_test = np.array([[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]])

my_x_train = np.array([[0,5],[5,0],[1,1],[2,2],[3,3]])
my_y_train = np.array([[1],[-1],[-1],[1],[1]])

my_x_test = np.array([[3,4]])
my_y_test = np.array([[1]])


def KNN_test(X_train, Y_train, X_test, Y_test, K):
    distances_list = []
    kth_neighbor_sum = 0
    correctly_classified = 0
    total = len(Y_test)

    #compute distance from test point t to all training sample
    for test_point in range(0, len(X_test)):
        for sample in range(0, len(X_train)):
            temp_distance = 0
            for dimension in range(0, len(X_test[0])):
                temp_distance = temp_distance + (X_train[sample][dimension]-X_test[test_point][dimension])**2

            distances_list.append([temp_distance, sample])

        distances_list.sort()

    #sum the labels of k-nearest-samples
        kth_neighbor_sum = 0
        for kth_neighbor in range(0, K):
            kth_neighbor_sum = kth_neighbor_sum + Y_train[distances_list[kth_neighbor][1]]

    #check if correctly classified
        if kth_neighbor_sum > 0:
            kth_neighbor_sum = 1
        else:
            kth_neighbor_sum = -1

        if Y_test[test_point][0] == kth_neighbor_sum:
            correctly_classified = correctly_classified+1

    #for all test points
        distances_list = []

    accuracy = correctly_classified/total
    return accuracy

def choose_K(X_train, Y_train, X_val, Y_val):
    best_k = 0
    best_accuracy = 0.0
    for current_k in range(1, len(X_train)+1):
        print(f"current_k: {current_k}")
        print(f"best_k: {best_k}")
        current_accuracy = KNN_test(X_train, Y_train, X_val, Y_val, current_k)
        print(f"current_accuracy: {current_accuracy}")
        print(f"best_accuracy: {best_accuracy}")
        if current_accuracy > best_accuracy:
            best_accuracy = current_accuracy
            best_k = current_k
            print("Update:")
            print(f"best_k: {best_k}")
            print(f"best_accuracy: {best_accuracy}")
        print("\n")


    print(f"best_k, best_accuracy: {best_k}, {best_accuracy}")

#choose_K(X_train, Y_train, X_test, Y_test)
#choose_K(my_x_train, my_y_train, X_test, Y_test)

print(KNN_test(X_train, Y_train, X_test, Y_test, 1))
print(KNN_test(X_train, Y_train, X_test, Y_test, 3))
print(KNN_test(X_train, Y_train, X_test, Y_test, 3))

#print(KNN_test(my_x_train, my_y_train, my_x_test, my_y_test, 3))
