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
    np.savetxt("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/CurrentFile" + str(num_file) +".csv",current_view,delimiter=",")
    file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListA_ans.txt", "a") 
    L = str(highest_priority) + "\n"
    file1.writelines(L) 
    file1.close()
if __name__ == "__main__":
    for i in range(10):
        list_A(MAX_OBJECTS,i)

        