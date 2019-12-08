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
    # getting V/H distance
    d1 = 10 # 1 * 10
    x_end = ending_position[0]
    y_end = ending_position[1]
    x_distance = abs(x - x_end)
    y_distance = abs(y - y_end)

    # getting diagonal distance
    d2 = 14 # sqrt(2) * 10
    diag_distance = abs(x_distance - y_distance)
    
    h = min(x_distance, y_distance) * d1 + diag_distance * d2
    return h

# function for printing the path? Might not need. Might use for changing the pixel values
# might need surrounding pixels of path to be green too. Too many pixels lol?
def print_path():
    return

# A* alg
def find_path_alg(img, w, h, starting_position, ending_position, path_color):
    # if the user chose the starting and ending position to be the same
    if is_destination(img, starting_position[0], starting_position[1], ending_position):
        print("The starting and ending position you have chosen is the same.")
        print("Exiting program.")
        exit()
    
    # creating a list to hold the f, g, and h values of the img
    # 5 for f, g, h values and parent x, y values
    node_details = np.full((w, h, 5), -1)

    # create a 2D-list that marks all nodes that have been evaluated by 1, 0 if not
    closed_list = np.zeros((w, h))
 
    # creating an open list that will contains nodes with calculated f costs
    # each index will contain: [f, [x, y]]
    open_list = []

    # putting the starting position in open list with its f as 0
    open_list.append([0.0, [starting_position[0], starting_position[1]]])

    while len(open_list) != 0:
        # set current equal to node with the lowest f-value
        if len(open_list) == 1:
            current = open_list[0]
        else:
            current = open_list[0]
            for node in range(open_list):
                # using <= since last appended nodes are the most recent and usually closer to end
                if node[0] <= current[0]:
                    current = node
                exit()

        # vars for current (x, y) for easier readability
        cur_x = current[1][0] 
        cur_y = current[1][1]

        # removing current node from open list
        open_list.remove(current)

        # appending (x, y) to closed list
        closed_list[cur_x][cur_y] = 1

        # checking if current node is the destination
        if is_destination(img, cur_x, cur_y, ending_position):
            print("Path has finished being calculated")
            return

        # getting the neighbor nodes
        else:
            neighbor_list_VH = [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]
            neighbor_list_diag = (cur_x - 1, cur_y + 1), (cur_x - 1, cur_y - 1), (cur_x + 1, cur_y + 1), (cur_x + 1, cur_y - 1)
                
            for neighbor in neighbor_list_VH:
                # vars for neighbor (x, y) for readability
                n_x = neighbor[0]
                n_y = neighbor[1]

                # check that neighbor exists, is traversable and is marked as 0 in closed list
                if (exists(img, n_x, n_y, w, h) and 
                    is_traversable(img, n_x, n_y) and 
                    closed_list[n_x][n_y] == 0):
                    # checking if current node is starting position in order to get right value g
                    if current[1] == starting_position:
                        g = 10
                    else: 
                        g = node_details[cur_x][cur_y][1] + 10
                    # getting other values
                    h = heuristics(img, n_x, n_y, ending_position)
                    f = g + h

                    # checking if f-cost to neighbor is shorter or if neighbor not in open list
                    
                    # storing details in node details
                    node_details[n_x][n_y][0] = f
                    node_details[n_x][n_y][1] = g
                    node_details[n_x][n_y][2] = h
                    node_details[n_x][n_y][3] = cur_x
                    node_details[n_x][n_y][4] = cur_y


