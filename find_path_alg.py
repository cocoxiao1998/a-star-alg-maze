# will be using A* algoritm
# Variables
# x: current width
# y: current height

import math
import numpy as np

# checks if node exists
def exists(img, x, y, w, h):
    if x < w and y < h:
        return True
    else: 
        return False

# checks if the node is traversable
def is_traversable(img, x, y):
    r = img[y][x][0]
    g = img[y][x][1]
    b = img[y][x][2]

    if r >= 250 and g >= 250 and b >= 250:
        return True
    else:
        return False

# checks if the destination has been reached
def is_destination(img, x, y, ending_position):
    if x == ending_position[0] and y == ending_position[1]:
        return True
    else:
        return False

# calculates heuristics (diagonal)
def heuristics(img, x, y, ending_position):
    # getting distance
    x_end = ending_position[0]
    y_end = ending_position[1]
    x_distance = abs(x - x_end)
    y_distance = abs(y - y_end)
    
    h = max(x_distance, y_distance)
    return h

# function for printing the path? Might not need. Might use for changing the pixel values
# might need surrounding pixels of path to be green too. Too many pixels lol?
def print_path():
    return

# A* alg
def find_path_alg(img, w, h, starting_position, ending_position, path_color):
    # if the user chose the starting and ending position to be the same
    if is_destination(img, starting_position[0], ending_position[1], ending_position):
        print("The starting and ending position you have chosen is the same.")
        print("Exiting program.")
        exit()
    
    # creating a list to hold the f, g, and h values of the img
    # 5 for f, g, h values and parent x, y values
    node_details = np.full((w, h, 5), -1)

    # create a list that stores all nodes that have been evaluated (part of the path now)
    closed_list = np.zeros((w, h))
 
    # create an open list that will contains nodes with calculated f costs
    # each index will contain: [f, [x, y]]
    open_list = []

    # putting the starting position in open list with its f as 0
    open_list.append([0.0, [starting_position[0], starting_position[1]]])

    # value for if the destination is reached
    # end = False

    while len(open_list) != 0:
        # temp node that contains the current node
        if len(open_list) == 1:
            current = open_list[0]
        else:
            for node in range(open_list):
                exit()
                print("hi")



    # returning
    print("Path has finished being calculated")

