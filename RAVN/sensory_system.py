# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

import csv

INPUT_FILE = "./ListD/CurrentFrame0.csv"
FRAME_PIXELS_X = 1280
FRAME_PIXELS_Y = 720
FRAME_AREA = FRAME_PIXELS_X * FRAME_PIXELS_Y

class VisualObject:
    def __init__(self, cx, cy, dx, dy, kind):
        self.cx = float(cx)
        self.cy = float(cy)
        self.dx = float(dx)
        self.dy = float(dy)
        self.kind = float(kind)

        self.bb_area = self.dx * self.dy

    def get_type(self):
        return self.kind

    def __repr__(self):
        return "% f" % self.kind

def get_objects():
    objects_list = []
    with open(INPUT_FILE, 'r') as frame:
        frame_reader = csv.reader(frame)
        for row in frame_reader:
            objects_list.append(VisualObject(row[0], row[1], row[2], row[3], row[4]))
    return objects_list
