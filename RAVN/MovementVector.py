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
#CLASS_PRIORITY = [5,4,3,2,1]
#FILENAME = r"robotCode\RAVN\Demo\Situation3.csv"
FILENAME = r"robotCode\RAVN\Demo\MoveDemo3.csv"
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720


class VisualObject:
    def __init__(self, cx, cy, dx, dy, type):
        self.cx = int(cx)
        self.cy = int(cy)
        self.dx = int(dx)
        self.dy = int(dy)
        self.type = int(type)

        self.bb_area = self.dx * self.dy

    def get_type(self):
        return self.type


def get_objects():
    objects_list = []
    with open(FILENAME, 'r') as frame:
        frame_reader = csv.reader(frame)
        for row in frame_reader:
            objects_list.append(VisualObject(row[0], row[1], row[2], row[3], row[4]))
    return objects_list


def acquire_target(objects_list):
    target = None
    for object_type in CLASS_PRIORITY:
        if target != None:
            break
        for item in objects_list:
            if item.type == object_type:
                if target == None:
                    target = item
                else:
                    if item.bb_area > target.bb_area:
                        target = item
    print("Acquired a target of type " + str(target.type))
    return target


# Returns movement vector in form [rotation_component, depth_component] where each value is in [-1, 0, 1].
# This will tell qualitatively which direcion the sub needs to move along each axis
def get_movement_vector(target_object):
    rotation_component = 0
    depth_component = 0
    if target_object.cx > ((FRAME_PIXELS_X/2) + 25):
        rotation_component = 1
        print("ROTATE RIGHT")
    elif target_object.cx < ((FRAME_PIXELS_X/2) - 25):
        rotation_component = -1
        print("ROTATE LEFT")
    else:
        print("DO NOT ROTATE")

    if target_object.cy > ((FRAME_PIXELS_Y/2) + 25):
        depth_component = 1
        print("ASCEND")
    elif target_object.cy < ((FRAME_PIXELS_Y/2) - 25):
        depth_component = -1
        print("DESCEND")
    else:
        print("DO NOT CHANGE DEPTH")

    return [rotation_component, depth_component]


frame_objects = get_objects()
target_object = acquire_target(frame_objects)
movement_vector = get_movement_vector(target_object)
