# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

import csv

#   Object numbers --> names
#   1: OBJECT_1
#   2: OBJECT_2
#   3: OBJECT_3
#   4: OBJECT_4
#   5: OBJECT_5
CLASS_PRIORITY = [1,2,3,4,5]
FILENAME = r"robotCode\RAVN\OILT Output Frames\CurrentFrame1.csv"
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720


class VisualObject:
    def __init__(self, cx, cy, dx, dy, type):
        self.cx = int(cx)
        self.cy = int(cy)
        self.dx = int(dx)
        self.dy = int(dy)
        self.type = type
    
    def get_type(self):
        return self.type


def get_type(obj):
    return obj.get_type()


def get_objects():
    objects_list = []
    with open(FILENAME, 'r') as frame:
        frame_reader = csv.reader(frame)
        for row in frame_reader:
            objects_list.append(VisualObject(row[0], row[1], row[2], row[3], row[4]))
    objects_list.sort(key=get_type)

    return objects_list

# Returns movement vector in form [rotation_command, depth_command] where each value is in [-1, 0, 1].
# This will tell qualitatively which direcion the sub needs to move along each axis
def get_movement_vector(target_object):
    movement_vector = [0, 0]

    if target_object.cx > FRAME_PIXELS_X/2:
        movement_vector[0] = 1
    elif target_object.cx < FRAME_PIXELS_X/2:
        movement_vector[0] = -1

    if target_object.cy > FRAME_PIXELS_Y/2:
        movement_vector[1] = 1
    elif target_object.cy < FRAME_PIXELS_Y/2:
        movement_vector[1] = -1
    return movement_vector


frame_objects = get_objects()
movement_vector = get_movement_vector(frame_objects[0])
print(movement_vector)