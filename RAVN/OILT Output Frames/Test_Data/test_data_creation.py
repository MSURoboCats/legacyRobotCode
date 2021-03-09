import numpy as np
import random as rd
MAX_OBJECTS = 6
CLASS_PRIORITY = [1, 3 , 4 ,5 ,2 ,6]
def list_A(tot_objects, num_file):
    #Note: To meet the specification set in Verification Plan the total number of objects must be greater than or equal to 4
    highest_priority_obj = 999
    highest_index = 999
    assert tot_objects >= 4, "Error: Total number of objects must be greater than or equal to 4"
    rows = rd.randint(4,tot_objects)
    current_view = np.empty([rows,5])
    classes = [*range(1,tot_objects+1)]
    for i in range(rows):
        current_view[i,0] = rd.randint(0,1280)
        current_view[i,1] = rd.randint(0,720)
        current_view[i,2] = rd.randint(0,1280)
        current_view[i,3] = rd.randint(0,720)
        obj_type = rd.choice(classes)
        for j in range(len(CLASS_PRIORITY)):
            if obj_type == CLASS_PRIORITY[j]:
                if j < highest_index:
                    highest_priority = CLASS_PRIORITY[j]
                    highest_index = j
        current_view[i,4] = obj_type
        classes.remove(obj_type)
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/ListA_ans.txt", "a") 
    L = str(highest_priority) + "\n"
    file1.writelines(L) 
    file1.close()

def list_B(num_file):
    centroid = np.array([rd.randint(0,1280), rd.randint(0,720)])
    if centroid[0] >= 576 and centroid[0] <= 704:
        directionX = "Forward, "
    elif centroid[0] < 576:
        directionX = "Left, "
    else:
        directionX = "Right, "
    if centroid[0] >= 324 and centroid[0] <= 396:
        directionY = "Forward"
    elif centroid[0] < 324:
        directionY = "Descend"
    else:
        directionY = "Ascend"
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/CurrentFile" + str(num_file) +".csv",centroid,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List B/ListB_ans.txt", "a") 
    L = directionX + directionY + "\n"
    file1.writelines(L) 
    file1.close()  
def list_C(tot_objects,num_file): 
    x = rd.randint(3,tot_objects)
    y = rd.randint(1,x)
    highest_priority_obj = 999
    highest_index = 999
    classes = [*range(1,tot_objects+1)]
    current_view = np.zeros([x,2])
    for i in range(x):
        obj_type = rd.choice(classes)
        current_view[i,0] = obj_type
        classes.remove(obj_type)
    classes = [*range(1,tot_objects+1)]
    for j in range(y):
        obj_type = rd.choice(classes)
        current_view[j,1] = obj_type
        classes.remove(obj_type)
    seen_list = current_view[0:y,1].tolist()
    print(seen_list)
    in_view_list = current_view[:,0].tolist()
    for a in range(len(in_view_list)):
        if in_view_list[a] not in seen_list and CLASS_PRIORITY.index(in_view_list[a]) < highest_index:
            highest_priority_obj = in_view_list[a]
            highest_index = a
    if highest_priority_obj == 999:
        highest_priority_obj = "Search"
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List C/ListC_ans.txt", "a") 
    L = str(highest_priority_obj) + "\n"
    file1.writelines(L) 
    file1.close() 
if __name__ == "__main__":
    for i in range(10):
        list_C(MAX_OBJECTS,i)
        