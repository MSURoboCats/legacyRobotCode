# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

from enum import Enum

import motor_system as ms
import sensory_system as ss

investigated_objects = []
novel_objects = []
relevant_types = [1, 2, 3, 4, 5]

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

# target_info shoud be in the form: [heading, type]
def acquire_target(target_info):
    # desired_heading = target_info[0]
    target_type = target_info[1]
    # TO DO: Attain desired heading with function to be made in motor_system.py
    objects_in_frame = ss.get_objects()
    # Verify that we can see the object we were looking for
    for item in objects_in_frame:
        if item.type == target_type:
            return item
    print("Failed to locate target object")
    return None

# Returns movement vector in form: [rotation_component, depth_component] where each value is in [-1, 0, 1].
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
            if item.type not in relevant_types:
                # TO DO: mark heading object was seen at
                novel_objects.append(item)       

def search(object_list):
    while(vehicle_state == State.SEARCH):
        for k in range(len(relevant_types)):
            if item.type == relevant_types[0]:
                relevant_types.remove(item.type)   
                return item.heading, item.type 
            else:                                       
                for item in object_list:                    
                    if item.type == relevant_types[k-1]:
                        relevant_types.remove(item.type)    
                        return item.heading, item.type
                    else:
                        return None                        
    else:
        ms.yawFunc()                                    

# target_info shoud be in the form [heading, type]
def investigate(target_info):
    target_object = acquire_target(target_info)
    while (target_object.bb_area < ss.FRAME_AREA):
        get_movement_vector(target_object)
        # TO DO: develop ability to actually move the sub to the target
    vehicle_state = State.SEARCH

def enact_state(argument):
    switcher = {
        State.SEARCH: search,
        State.INVESTIGATE: investigate
    }
    action = switcher.get(argument, lambda: "Invalid state")
    action()

if __name__ == "__main__":
    vehicle_state = None
    while vehicle_state != State.TASK_COMPLETED:
        enact_state(vehicle_state)
    print("All tasks completed")
