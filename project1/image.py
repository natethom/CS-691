import numpy as np
from PIL import Image

def KNN_test(X_train, Y_train, X_test, Y_test, K):
    distances_list = []
    kth_neighbor_sum = 0
    correctly_classified = 0
    total = len(Y_test)

    #compute distance from test point t to all training sample
    for test_point in range(0, len(X_test)):
        for sample in range(0, len(X_train)):
            temp_distance = (
            (X_train[sample][0]-X_test[test_point][0])**2+
            (X_train[sample][1]-X_test[test_point][1])**2
            )**(.5)

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

im = Image.open('~/Downloads/digit.jpg') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
