# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

from enum import Enum

import motor_system as ms
import sensory_system as ss

CLASS_PRIORITY = [1,2,3,4,5]

investigated_objects = []
novel_objects = []
seen_objects = []

class State(Enum):
    SEARCH = 1
    INVESTIGATE = 2
    TASK_COMPLETED = 3

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
    if target_object.cx > ((ss.FRAME_PIXELS_X/2) + 25):
        rotation_component = 1
        print("ROTATE RIGHT")
    elif target_object.cx < ((ss.FRAME_PIXELS_X/2) - 25):
        rotation_component = -1
        print("ROTATE LEFT")
    else:
        print("DO NOT ROTATE")

    if target_object.cy > ((ss.FRAME_PIXELS_Y/2) + 25):
        depth_component = 1
        print("ASCEND")
    elif target_object.cy < ((ss.FRAME_PIXELS_Y/2) - 25):
        depth_component = -1
        print("DESCEND")
    else:
        print("DO NOT CHANGE DEPTH")

    return [rotation_component, depth_component]

def update_known_objects(object_list):
    for item in object_list:
        if item.type not in investigated_objects:
            if item.type not in seen_objects:
                # TO DO: mark heading object was seen at
                novel_objects.append(item)       

def search(object_list):
    if completed_rotation():                            # check if the rotation has been completed
        for k in range(len(CLASS_PRIORITY)):            # iterate through class priority array
            for item in object_list:                    # iterate through the object list
                if item.type == CLASS_PRIORITY[k-1]:    # check if the object in class priority list is contained in the object list
                    return item                         # if it is found return it
    else:
        ms.yawFunc()                                    # if the rotation is not complete, keep spinning

if __name__ == "__main__":
    vehicle_state = None
