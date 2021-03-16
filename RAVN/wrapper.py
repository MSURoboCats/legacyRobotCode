import sensory_system as ss
import central_nervous_system as cs

def test_1_1_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        object_list = ss.get_objects(filepath + str(i) + ".csv")
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_1_1.txt", "a") 
        L = str(object_list) + "\n"
        file1.writelines(L) 
        file1.close() 

def test1_2_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects()
        target = cs.search(object_list)
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_2_1.txt", "a") 
        L = str(target) + "\n"
        file1.writelines(L) 
        file1.close() 

if __name__ == '__main__':
    # test_1_1_1()
    test1_2_1()