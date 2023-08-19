from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import random

# ============ THE MID POINT LINE ALGO ========== #
def findzone(x1,y1,x2,y2):

    dy = y2-y1
    dx = x2-x1

    if (abs(dx)>abs(dy)):
        if dx>=0 and dy>=0:
            return 0
        elif dx<=0 and dy>=0:
            return 3
        elif dx>=0 and dy<=0:
            return 7
        elif dx<=0 and dy<=0:
            return 4
    else:
        if dx>=0 and dy>=0:
            return 1
        elif dx<=0 and dy>=0:
            return 2
        elif dx>=0 and dy<=0:
            return 6
        elif dx<=0 and dy<=0:
            return 5


def convert_to_zone_0(x,y,zone):

    new_x = 0
    new_y = 0

    if zone==0:
        new_x = x
        new_y = y
    elif zone==1:
        new_x = y
        new_y = x
    elif zone==2:
        new_x = y
        new_y = -x
    elif zone==3:
        new_x = -x
        new_y = y
    elif zone==4:
        new_x = -x
        new_y = -y
    elif zone==5:
        new_x = -y
        new_y = -x
    elif zone==6:
        new_x = -y
        new_y = x
    elif zone==7:
        new_x = x
        new_y = -y

    return new_x,new_y

def convert_to_org_zone(x,y,zone):

    new_x = 0
    new_y = 0

    if zone==0:
        new_x = x
        new_y = y
    elif zone==1:
        new_x = y
        new_y = x
    elif zone==2:
        new_x = -y
        new_y = x
    elif zone==3:
        new_x = -x
        new_y = y
    elif zone==4:
        new_x = -x
        new_y = -y
    elif zone==5:
        new_x = -y
        new_y = -x
    elif zone==6:
        new_x = y
        new_y = -x
    elif zone==7:
        new_x = x
        new_y = -y

    return new_x,new_y


def mid_point_line(x1,y1,x2,y2):

    zone = findzone(x1, y1, x2, y2)

    x1, y1 = convert_to_zone_0(x1, y1, zone)
    x2, y2 = convert_to_zone_0(x2, y2, zone)

    dy = y2-y1
    dx = x2-x1
    d = 2*dy-dx

    incE = 2*dy
    incNE = 2*(dy-dx)

    x = x1
    y = y1

    while x<=x2:
        x += 1
        if d<=0:
            d = d+incE
        else:
            y+=1
            d = d + incNE
        drawn_x,drawn_y = convert_to_org_zone(x,y,zone)
        draw_points(drawn_x,drawn_y)

#---------------------------------------------------#

# ============ THE MID POINT CIRCLE ALGO ========== #

def generate_origin_circle(radius):

    points_of_circle= []
    d = 1-radius
    x = 0
    y = radius
    while x<y:
        points_of_circle.append((x, y))
        if d<0:
            d= (d+2*x+3)
            x+=1
        else:
            d= (d+2*x-2*y+5)
            x+=1
            y-=1
    return points_of_circle

# ================================================= #

# ================= ZONE CONVERSION =============== #
def ConvertToZone0(x,y):
    new_x = y
    new_y = x
    return new_x,new_y
def ConvertToZone2(x,y):
    new_x = -x
    new_y = y
    return new_x,new_y
def ConvertToZone3(x,y):
    new_x = -y
    new_y = x
    return new_x,new_y
def ConvertToZone4(x,y):
    new_x = -y
    new_y = -x
    return new_x,new_y
def ConvertToZone5(x,y):
    new_x = -x
    new_y = -y
    return new_x,new_y
def ConvertToZone6(x,y):
    new_x = x
    new_y = -y
    return new_x,new_y
def ConvertToZone7(x,y):
    new_x = y
    new_y = -x
    return new_x,new_y
# ================================================= #

# ============== DRAWING FUNCTION ================= #

def drawCircle(center_x,center_y,radius):

    points_of_circle_zone_1 = generate_origin_circle(radius)

    #DRAWING ZONE-1
    for coord in points_of_circle_zone_1:
        drawn_x = coord[0]+center_x
        drawn_y = coord[1]+center_y
        draw_points(drawn_x,drawn_y)

    #DRAWING ZONE-0
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone0(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-2
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone2(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-3
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone3(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-4
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone4(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-5
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone5(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-6
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone6(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

    #DRAWING ZONE-7
    for coord in points_of_circle_zone_1:
        converted_x,converted_y = ConvertToZone7(coord[0],coord[1])
        drawn_x = converted_x + center_x
        drawn_y = converted_y + center_y
        draw_points(drawn_x, drawn_y)

# ================================================= #



#--------------DRAWING FUNCTIONS--------------#

def drawFilledCircle(x,y,r):

    for i in range(1,r+1):
        drawCircle(x, y, i)

def drawFilledQuad(x1,y1,x3,y3):

    for i in range(int(x1),int(x3+1)):
        mid_point_line(i,y1,i,y3)


# Global variables
craft_position = np.array([0, 0]) #craft position
step_size = 10.0 #translation step size
scale_factor = 0.2 #initial size
scale_rate = 0.001 #scale rate


def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def transform():
    global craft_position, scale_factor

    glClear(GL_COLOR_BUFFER_BIT)

    #-----------------BACKGROUND---------------#

    # WHITE STARS
    glColor3f(1, 1, 1)
    for i in range(0,10):
        draw_points(random.randint(1, 1000),random.randint(1, 1000))

    # YELLOW STARS
    glColor3f(0.6, 0.6, 0)
    for i in range(0,10):
        draw_points(random.randint(1, 1000),random.randint(1, 1000))

    # ASTEROIDS
    glColor3f(0.26, 0.16, 0.055)
    for i in range(0,9):
        spawn_coord = (random.randint(1, 1000), random.randint(1, 1000))
        drawFilledCircle(spawn_coord[0],spawn_coord[1],random.randint(1, 15))

    #-----------------BIG STARS IN THE BACKGROUND-----------------#

    #----------------YELLOW STAR-----------------#
    sc = scale_factor
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])

    # YELLOW STAR
    y_sun_v1 = np.array([[-300],
                   [50],
                   [1]])

    y_sun_v3 = np.array([[-200],
                   [150],
                   [1]])

    y_sun_v1 = np.matmul(s, y_sun_v1)
    y_sun_v3 = np.matmul(s, y_sun_v3)

    glColor3f(0.992, 0.722, 0.075)
    drawFilledQuad(int(y_sun_v1[0][0] + 500),
                   int(y_sun_v1[1][0] + 500),
                   int(y_sun_v3[0][0] + 500),
                   int(y_sun_v3[1][0] + 500))

    # ----------------RED STAR-----------------#

    r_sun_v1 = np.array([[400],
                       [-200],
                       [1]])

    r_sun_v3 = np.array([[450],
                       [-250],
                       [1]])

    r_sun_v1 = np.matmul(s, r_sun_v1)
    r_sun_v3 = np.matmul(s, r_sun_v3)

    glColor3f(0.863, 0.282 , 0.149)
    drawFilledQuad(int(r_sun_v1[0][0] + 500),
                   int(r_sun_v1[1][0] + 500),
                   int(r_sun_v3[0][0] + 500),
                   int(r_sun_v3[1][0] + 500))

    # ----------------BLUE STAR-----------------#

    b_sun_v1 = np.array([[20],
                         [0],
                         [1]])

    b_sun_v3 = np.array([[40],
                         [20],
                         [1]])

    b_sun_v1 = np.matmul(s, b_sun_v1)
    b_sun_v3 = np.matmul(s, b_sun_v3)

    glColor3f(0, 0.110, 0.584)
    drawFilledQuad(int(b_sun_v1[0][0] + 500),
                   int(b_sun_v1[1][0] + 500),
                   int(b_sun_v3[0][0] + 500),
                   int(b_sun_v3[1][0] + 500))


    #-------------SPACE CRAFT------------------#
    space_craft_base_v1 = np.array([[-50],
                   [20],
                   [1]])

    space_craft_base_v3 = np.array([[100],
                   [-20],
                   [1]])

    space_craft_window_v1 = np.array([[-35],
                                    [10],
                                    [1]])

    space_craft_window_v3 = np.array([[85],
                                    [-10],
                                    [1]])

    space_craft_window_feet_left_v1 = np.array([[-25],
                                    [-20],
                                    [1]])
    space_craft_window_feet_left_v3 = np.array([[-20],
                                    [-35],
                                    [1]])

    space_craft_window_feet_right_v1 = np.array([[70],
                                                [-20],
                                                [1]])
    space_craft_window_feet_right_v3 = np.array([[75],
                                                [-35],
                                                [1]])

    space_craft_hub_v1 = np.array([[-25],
                                      [40],
                                      [1]])

    space_craft_hub_v3 = np.array([[75],
                                      [23],
                                      [1]])

    space_craft_hub_window_v1 = np.array([[-20],
                                   [35],
                                   [1]])

    space_craft_hub_window_v3 = np.array([[70],
                                   [28],
                                   [1]])
    glColor3f(0.7, 0.7, 0.7)
    drawFilledQuad(space_craft_base_v1[0][0] + 500 + craft_position[0],
                   space_craft_base_v1[1][0] + 500 + craft_position[1],
                   space_craft_base_v3[0][0] + 500 + craft_position[0],
                   space_craft_base_v3[1][0] + 500 + craft_position[1])
    glColor3f(1, 1, 0)
    drawFilledQuad(space_craft_window_v1[0][0] + 500 + craft_position[0],
                   space_craft_window_v1[1][0] + 500 + craft_position[1],
                   space_craft_window_v3[0][0] + 500 + craft_position[0],
                   space_craft_window_v3[1][0] + 500 + craft_position[1])
    glColor3f(0.7, 0.7, 0.7)
    drawFilledQuad(space_craft_window_feet_left_v1[0][0] + 500 + craft_position[0],
                   space_craft_window_feet_left_v1[1][0] + 500 + craft_position[1],
                   space_craft_window_feet_left_v3[0][0] + 500 + craft_position[0],
                   space_craft_window_feet_left_v3[1][0] + 500 + craft_position[1])

    drawFilledQuad(space_craft_window_feet_right_v1[0][0] + 500 + craft_position[0],
                   space_craft_window_feet_right_v1[1][0] + 500 + craft_position[1],
                   space_craft_window_feet_right_v3[0][0] + 500 + craft_position[0],
                   space_craft_window_feet_right_v3[1][0] + 500 + craft_position[1])

    drawFilledQuad(space_craft_hub_v1[0][0] + 500 + craft_position[0],
                   space_craft_hub_v1[1][0] + 500 + craft_position[1],
                   space_craft_hub_v3[0][0] + 500 + craft_position[0],
                   space_craft_hub_v3[1][0] + 500 + craft_position[1])
    glColor3f(1, 1, 1)
    drawFilledQuad(space_craft_hub_window_v1[0][0] + 500 + craft_position[0],
                   space_craft_hub_window_v1[1][0] + 500 + craft_position[1],
                   space_craft_hub_window_v3[0][0] + 500 + craft_position[0],
                   space_craft_hub_window_v3[1][0] + 500 + craft_position[1])
    #----------------------------------------------------------------------------#



def showScreen():
    global scale_factor

    scale_factor += scale_rate

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    transform()

    glutSwapBuffers()


def handle_key(key, x, y):
    global craft_position, step_size

    if key == b'w':
        craft_position[1] += step_size
    elif key == b's':
        craft_position[1] -= step_size
    elif key == b'a':
        craft_position[0] -= step_size
    elif key == b'd':
        craft_position[0] += step_size

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Movable SpaceCraft")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(handle_key)
glutMainLoop()
