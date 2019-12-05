# will be using A* algoritm
# Variables
# x: current width
# y: current height

def find_path_alg(img, w, h, starting_position, ending_position, path_color):
    print("Path has finished being calculated")

# checks if the pixel value exists
def exists(img, x, y, w, h):
    if x < w and y < h:
        return True
    else: 
        return False

# checks if the pixel value is traversable
def traversable(img, x, y):
    r = img[y][x][0]
    g = img[y][x][1]
    b = img[y][x][2]

    if r >= 250 and g >= 250 and b >= 250:
        return True
    else:
        return False

# checks if the destination has been reached
def destination(img, x, y, ending_position):
    if x == ending_position[0] and y == ending_position[1]:
        return True
    else:
        return False

# calculates heuristics (diagonal)
def heuristics(img, x, y, ending_position):
    h = google
    return h