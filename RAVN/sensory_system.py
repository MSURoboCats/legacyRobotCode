# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

from enum import Enum

import central_nervous_system as cns
import motor_system as ms

INPUT_FILE = r"robotCode\RAVN\Demo\MoveDemo3.csv"
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720

class ObjectType(Enum):
    OBJECT_1 = 1
    OBJECT_2 = 2
    OBJECT_3 = 3
    OBJECT_4 = 4
    OBJECT_5 = 5

def get_objects():
    objects_list = []
    with open(INPUT_FILE, 'r') as frame:
        frame_reader = csv.reader(frame)
        for row in frame_reader:
            objects_list.append(VisualObject(row[0], row[1], row[2], row[3], row[4]))
    return objects_list