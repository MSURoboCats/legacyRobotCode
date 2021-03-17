# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

#import motor_system as ms
import sensory_system as ss

object_priority = [1,3,4,5,2,6]
frame_objects = []
target_object = None

def acquire_target():
    for k in range(len(object_priority)):       
        for item in frame_objects:                    
            if item.kind == object_priority[k]:
                return item                                                     
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

def search():
    #maneuver to find new object
    return

def check_target_in_frame():     
    for item in frame_objects:                    
        if item.kind == target_object.kind:
            return True
    return False

def check_investigated():
    if target_object.dx > (ss.FRAME_PIXELS_X * .8) or target_object.dy > (ss.FRAME_PIXELS_Y * .8):
        return True
    else:
        return False

##while object_priority:
##    print("Getting objects from CSV")
##    frame_objects = ss.get_objects()
##    if target_object:
##        print("Target object already exists")
##        if check_target_in_frame():
##            print("Target is in frame")
##            if check_investigated():
##                print("Marking object as investigated")
##                object_priority.remove(target_object.kind)
##                target_object = None
##            else:
##                #print("Target is not yet investigated")
##                get_movement_vector(target_object)
##        else:
##            print("Target is NOT in frame -- Lost target object")
##            target_object = None
##    else:
##        print("Target object doesn't already exist - Aquiring Target")
##        target_object = acquire_target()
##        if target_object:
##            print("Successfully aquired target")
##            get_movement_vector(target_object)
##        else:
##            print("No potential target -- entering search state")
##            search()
##    print("")
##
##print("")
##print("----------------------------------------------------------")
##print("All objects have been investigated. Terminating operation.")
##print("----------------------------------------------------------")
