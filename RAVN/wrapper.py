import sensory_system as ss
import central_nervous_system as cs

def test_1_1_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects()
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_1_1.txt", "a") 
        L = str(object_list) + "\n"
        file1.writelines(L) 
        file1.close() 

def test1_2_1():
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects().copy()
        target = cs.search(object_list)
        cs.relevant_types = [1, 3 , 4 ,5 ,2 ,6]
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1_2_1.txt", "a") 
        L = str(target) + "\n"
        file1.writelines(L) 
        file1.close()
        print(i)

def test1():
    diff_priorities = [[1,2,3,4,5,6],[2,3,4,5,6,1],[3,4,5,6,1,2],[4,5,6,1,2,3],[5,6,1,2,3,4]]
    filepath = "C:/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/CurrentFile"
    for i in range(100):
        if i % 20 == 0:
            obj_priority = diff_priorities[int(i/20)].copy()
        cs.relevant_types = obj_priority.copy()
        print(cs.relevant_types)
        ss.INPUT_FILE = filepath + str(i) + ".csv"
        object_list = ss.get_objects()
        target = cs.search(object_list)
        file1 = open("/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/List A/Test1.txt", "a") 
        L = str(target) + "\n"
        file1.writelines(L) 
        file1.close()
        print(i)
def test3_2_1():
    test_amount = 50
    filepath = "/Users/kyler/OneDrive/Documents/Capstone/robotCode/RAVN/OILT Output Frames/Test_Data/ListD/"
    file1 = open(filepath + "ResultsD.txt", "w")
    tests_passed = 0
    for i in range(test_amount):
        file1.writelines("#### Test " + str(i) + " ####\r")
        ss.INPUT_FILE = filepath + "CurrentFrame" + str(i) + ".csv"
        objects_in_frame = ss.get_objects().copy()
        while cs.relevant_types:
            objects_in_frame = ss.get_objects().copy()
            if cs.target_object:
                if cs.check_target_in_frame():
                    if cs.check_investigated():
                        cs.relevant_types.remove(cs.target_object.type)
                        L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None
                    else:
                        cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                        L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                        file1.writelines(L)
                        cs.target_object = None #REMOVE IN ACTUAL OPERATION
                else:
                    L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                    file1.writelines(L)
                    cs.target_object = None
            else:
                cs.target_object = cs.acquire_target()
                if cs.target_object:
                    pass
                else:
                    L = "Searching...\r\r"
                    file1.writelines(L)
                    break

        if cs.relevant_types:
            ss.INPUT_FILE = filepath + "/NextFrame" + str(i) + ".csv"
            file1.writelines("# NextFrame" + str(i) + ".csv\r")

            while cs.relevant_types:
                cs.objects_in_frame = ss.get_objects().copy()
                if cs.target_object:
                    if cs.check_target_in_frame():
                        if cs.check_investigated():
                            cs.object_priority.remove(cs.target_object.type)
                            L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None
                        else:
                            cs.relevant_types.remove(cs.target_object.type) #REMOVE IN ACTUAL OPERATION
                            L = "Chosen Object Type: " + str(cs.target_object.type) + "\r"
                            file1.writelines(L)
                            cs.target_object = None #REMOVE IN ACTUAL OPERATION
                    else:
                        L = "Chosen Object of type " + str(cs.target_object.type) + " has been lost.\r"
                        file1.writelines(L)
                        cs.target_object = None
                else:
                    cs.target_object = cs.acquire_target()
                    if cs.target_object:
                        pass
                    else:
                        L = "Searching...\r\r"
                        tests_passed += 1
                        file1.writelines(L)
                        break

        else:
            tests_passed += 1
            file1.writelines("All objects are investigated. Program exited.\r")
            file1.writelines("\r")

    file1.writelines("------------------------------------------------------\r")
    file1.writelines(str(tests_passed) + " of " + str(test_amount) + " tests passed.\r")
    file1.close()

        
if __name__ == '__main__':
    # test_1_1_1()
    # test1_2_1()

    test1()
    # test3_2_1()