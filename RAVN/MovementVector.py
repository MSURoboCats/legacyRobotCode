FILENAME = "inputs.csv"

import csv
import numpy as np 

class ObjectOfInterest:
    def __init__(self, number, cx, cy, dx, dy):
        self.number = number
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy


def sortCriteria(obj):
    return obj.number


def prioritizeObjects():
    with open(FILENAME, "r") as frame:
        reader = csv.reader(frame)
        for row in reader:
            objects.append(ObjectOfInterest(row[0], row[1], row[2], row[3], row[4]))
    objects.sort(key=sortCriteria)


class_priority = [1,2,3,4,5]
objects = []