# cannot traverse/black = values below "[5, 5, 5]"
# can traverse/white = values above "[250, 250, 250]" 

import cv2

# global variables
flag = 0
img = cv2.imread("campus_map.jpg")
window_name = "Campus Map"
starting_position = list()
ending_position = list()
path_color = (0, 255, 0)

def main():

    global img
    global window_name

    # displaying the image in a window for a user to choose a starting position
    print("Choose a valid starting position (white pixel) by double left clicking on the image.")
    print("Click any key to exit out of this program at any time.")

    dimensions = img.shape
    h = dimensions[0]
    w = dimensions[1]

    cv2.imshow(window_name, img)
    cv2.setMouseCallback(window_name, mouse_events)
    cv2.waitKey(0)

def mouse_events(event, x, y, flags, param):
    global flag
    global img
    global starting_position
    global ending_position
    global path_color

    if event == cv2.EVENT_LBUTTONDBLCLK:
        # need to check if rgb values correspond to the color white
        r = img[y][x][0]
        g = img[y][x][1]
        b = img[y][x][2]
        color_flag = 0
        if r >= 250 and g >= 250 and b >= 250:
            color_flag = 1
        else:
            print("You have chosen an invalid position. Choose a valid one.")

        # getting starting position
        if flag == 0 and color_flag == 1:
            cv2.imshow(window_name, img)
            print("The starting position you chose was: (%d, %d)" % (x, y))
            starting_position.append(x)
            starting_position.append(y)
            img[y, x] = path_color
            flag += 1
        # getting ending position
        elif flag == 1 and color_flag == 1:
            cv2.imshow(window_name, img)
            print("The ending position you chose was: (%d, %d)" % (x, y))
            ending_position.append(x)
            ending_position.append(y)

            # calling function to find path
            path()
            flag += 1
            
def path():


    # calling function to save the new image
    save_file()

def save_file():
    global img
    # writing the final image as user inputted filename
    filename = input("Enter a filename for the image to save as: ")
    try:
        cv2.imwrite(filename, img)
    except:
        print("There was an error saving the image. Exiting program.")
        exit()

    print("The image was successfully saved. Exiting program.")
    exit()
    

if __name__ == "__main__":
    main()

