import csv
import os
import math
from statistics import mean

det = []
img = []
with open("result_bins.txt") as f:
    c = csv.reader(f, delimiter=' ', skipinitialspace=True)
    for line in c:
        if line != []:
            if line[-1] == 'milli-seconds.':
                det.append(['new_image'])
                img.append(line)
            if line[0] == 'Bins:':
                line[1] = line[1].split('\t')[0]
                line[8] = line[8].split(')')[0]
                line[2] = float(line[2])/float(640)
                line[4] = float(line[4])/float(480)
                line[6] = float(line[6])/float(640)
                line[8] = float(line[8])/float(480)
                det.append(line)
# up till here, we have line[2] as top left corner's x coordinate,
# line[4] as the top left corner's y coordinate,
# line[6] as the width,
# line[8] as the height,
# all in ratio numbers

for line in det:
    if line[0] == 'Bins:':
        line[2] = line[2]+line[6]/2
        line[4] = line[4]+line[8]/2
        line.remove(line[0])
        line.remove(line[0])
        line.remove(line[1])
        line.remove(line[2])
        line.remove(line[3])


gro = []
for file in os.listdir("C:/Users/xingz/OneDrive/Desktop/test_bin"):
    if file.endswith(".txt"):
        gro.append(['new_image'])
        with open(os.path.join("C:\\Users\\xingz\\OneDrive\\Desktop\\test_bin",file)) as f:
            c = csv.reader(f, delimiter=' ', skipinitialspace=True)
            for line in c:
                gro.append(line[1:])
# now we have both the ground truth and the detections, in the same format

gro_pro = []
while ['new_image'] in gro:
    gro.remove(gro[gro.index(['new_image'])])
    if ['new_image'] in gro:
        gro_pro.append(gro[0:gro.index(['new_image'])])
        gro = gro[gro.index(['new_image']):]
    else:
        gro_pro.append(gro[0:])

det_pro = []
while ['new_image'] in det:
    det.remove(det[det.index(['new_image'])])
    if ['new_image'] in det:
        det_pro.append(det[0:det.index(['new_image'])])
        det = det[det.index(['new_image']):]
    else:
        det_pro.append(gro[0:])
# now we have detection and ground truth all in kind of a "cell array",
# det_pro[i] indicates detection results in i th image
# gro_pro[i] indicates ground truth in i th image
# det_pro[i][j] indicates the j th bounding box in i th image
# gro_pro[i][j] indicates the j th bounding box in i th image

accurate_amount = 0
total_amount = 200
for i in range(0, total_amount):
    det_c = det_pro[i]
    gro_c = gro_pro[i]
     # number of objects in the prediction image
    if len(gro_c) == len(det_c):
        accurate_amount = accurate_amount+1
        
print('The accuracy for the number of bins in the image is:')
print(accurate_amount/total_amount*100, '%')
