import numpy as np

training_set_1_x = np.array([[0,1], [0,0], [1,0], [0,0], [1,1]])
training_set_1_y = np.array([[1, 0, 0, 0, 1]])

validation_set_1_x = np.array([[0,0], [0,1], [1,0], [1,1]])
validation_set_1_y = np.array([[0, 1, 0, 1]])

testing_set_1_x = np.array([[0,0], [0,1], [1,0], [1,1]])
testing_set_1_y = np.array([[1, 1, 0, 1]])

set_1_tree = {"Node1": {}}

training_set_2_x = np.array([[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,1], [1,1,0,1], [1,1,0,0], [1,0,0,1], [0,1,0,1], [0,1,0,0]])
training_set_2_y = np.array([[0, 1, 0, 0, 1, 0, 1, 1, 1]])

validation_set_2_x = np.array([[1,0,0,0], [0,0,1,1], [1,1,0,1], [1,1,0,0], [1,0,0,1], [0,1,0,0]])
validation_set_2_y = np.array([[0, 0, 1, 0, 1, 1]])

testing_set_2_x = np.array([[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,1], [1,1,0,1], [1,1,0,0], [1,0,0,1], [0,1,0,1], [0,1,0,0]])
testing_set_2_y = np.array([[1, 1, 0, 0, 1, 0, 1, 1, 1]])


class Decision_Tree_Node:
    def __init__(self, feature_data, label_data, feature_index):
        self.no_branch = None
        self.yes_branch = None

        self.leaf_output = "blank_leaf"

        self.feature_index = 0

    def Print_Decision_Tree(self):
        if(self.no_branch == None and self.yes_branch == None):
            print(self.leaf_output),
        else:
            if self.no_branch:
                self.no_branch.Print_Decision_Tree()
            else:
                print("Missing no_branch")

            print(f"Featue Data: {self.feature_data}"),
            print(f"Label Data: {self.label_data}"),

            if self.yes_branch:
                self.yes_branch.Print_Decision_Tree()
            else:
                print("Missing yes_branch")

class Decision_Tree:
    def __init__(self, feature_data, label_data, ):
        self.feature_data = feature_data
        self.label_data = label_data
        self.decision_tree_root_node = None

    def Print_Decision_Tree(self):
        if self.decision_tree_root_node == None:
            print("There are no nodes in the decision tree.")
        else:
            self.decision_tree_root_node.Print_Decision_Tree()

    def Add_Node(self, feature_index):
        if self.decision_tree_root_node == None:
            self.decision_tree_root_node = Decision_Tree_Node(self.feature_data, self.label_data, feature_index)

def DT_train_binary(X,Y,max_depth):
    #1. Make F decision trees for number of features
    number_of_features = len(X[0])
    number_of_samples = len(X)

    #create list to hold possible decision trees
    possible_decision_trees = []

    #for number of features, 'f', create 'f' decision trees
    for feature in range(0, number_of_features):
        temp_decision_tree = Decision_Tree(X, Y)
        temp_decision_tree.Add_Node(feature)

        #for number of samples split the data accordingly into 'f'
        ##decision trees

        possible_decision_trees.append(temp_decision_tree)

    for feature in range(0, number_of_features):
        possible_decision_trees[feature].Print_Decision_Tree()
    #2. Determine accuracy of each tree based on training data

    #3. Select tree with greatest accuracy on training

    #4. check for 100% (if 100 then tree is complete)

    #5 split data

    #6. repeat until convergence

# def DT_train_binary(X,Y,max_depth):
#     #1. Make F decision trees for number of features
#     number_of_features = len(X[0])
#     number_of_samples = len(X)
#
#     #create list to hold possible decision trees
#     possible_decision_trees = []
#
#     #for number of features, 'f', create 'f' decision trees
#     for feature in range(0, number_of_features):
#         #add a dictionary with a key 'feature' whose value is the corresponding
#         ##feature's number in the list of features
#         possible_decision_trees.append({'feature': feature})
#
#         #add key 'no_branch' to each feature's dictionary
#         possible_decision_trees[feature]['no_branch'] = {}
#
#         #add key 'yes_branch' to each feature's dictionary
#         possible_decision_trees[feature]['yes_branch'] = {}
#
#         #add key 'data' to each 'no_branch' dictionary
#         possible_decision_trees[feature]['no_branch']['data'] = []
#
#         #add key 'data' to each 'yes_branch' dictionary
#         possible_decision_trees[feature]['yes_branch']['data'] = []
#
#         #for number of samples split the data accordingly into 'f'
#         ##decision trees
#         for sample in range(0, number_of_samples):
#             #if the current sample's feature is 0 the data into no_branch
#             if X[sample][feature] == 0:
#                 possible_decision_trees[feature]['no_branch']['data'].append(X[sample])
#             else:
#             #else put the data into yes_branch
#                 possible_decision_trees[feature]['yes_branch']['data'].append(X[sample])
#
#     print(possible_decision_trees, "\n")
#     print(possible_decision_trees[0], "\n")
#     print(possible_decision_trees[0]['no_branch'], "\n")
#     print(possible_decision_trees[0]['no_branch']['data'], "\n")
#     print(possible_decision_trees[0]['no_branch']['data'][0], "\n")
#     print(possible_decision_trees[0]['no_branch']['data'][0][0], "\n")
#
#
#
#
#     #2. Determine accuracy of each tree based on training data
#
#     #3. Select tree with greatest accuracy on training
#
#     #4. check for 100% (if 100 then tree is complete)
#
#     #5 split data
#
#     #6. repeat until convergence

DT_train_binary(training_set_1_x, training_set_1_y, -1)




# a = [(1, 1), (2, 1), (3, 1), (4, 3), (5, 3), (6, 3), (7, 7), (8, 7), (9, 7)]
#
# # pass 1: create nodes dictionary
# nodes = {}
# for i in a:
#     id, parent_id = i
#     nodes[id] = { 'id': id }
#     print(f"nodes: {nodes}\n")
#
# # pass 2: create trees and parent-child relations
# forest = []
# for i in a:
#     id, parent_id = i
#     node = nodes[id]
#
#     # either make the node a new tree or link it to its parent
#     if id == parent_id:
#         # start a new tree in the forest
#         forest.append(node)
#     else:
#         # add new_node as child to parent
#         parent = nodes[parent_id]
#         if not 'children' in parent:
#             # ensure parent has a 'children' field
#             parent['children'] = []
#         children = parent['children']
#         children.append(node)
#
# print (forest)
