import sensory_system as ss
import central_nervous_system as cs

test_amount = 50

def test3_2_1():
    file1 = open("./ListD/ResultsD.txt", "w")
    tests_passed = 0
    for i in range(test_amount):
        file1.writelines("#### Test " + str(i) + " ####\r")
        cs.object_priority = [1,3,4,5,2]
        cs.frame_objects = []
        cs.target_object = None

        ss.INPUT_FILE = "./ListD/CurrentFrame" + str(i) + ".csv"
        file1.writelines("# CurrentFrame" + str(i) + ".csv\r")

        while cs.object_priority:
            cs.frame_objects = ss.get_objects()
            if cs.target_object:
                if cs.check_target_in_frame():
                    if cs.check_investigated():
                        cs.object_priority.remove(cs.target_object.kind)
                        L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                        file1.writelines(L)
                        cs.target_object = None
                    else:
                        cs.object_priority.remove(cs.target_object.kind) #REMOVE IN ACTUAL OPERATION
                        L = "Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                        file1.writelines(L)
                        cs.target_object = None #REMOVE IN ACTUAL OPERATION
                else:
                    L = "Chosen Object of type " + str(cs.target_object.kind) + " has been lost.\r"
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
                
        if cs.object_priority:
            ss.INPUT_FILE = "./ListD/NextFrame" + str(i) + ".csv"
            file1.writelines("# NextFrame" + str(i) + ".csv\r")

            while cs.object_priority:
                cs.frame_objects = ss.get_objects()
                if cs.target_object:
                    if cs.check_target_in_frame():
                        if cs.check_investigated():
                            cs.object_priority.remove(cs.target_object.kind)
                            L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                            file1.writelines(L)
                            cs.target_object = None
                        else:
                            cs.object_priority.remove(cs.target_object.kind) #REMOVE IN ACTUAL OPERATION
                            L = "Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                            file1.writelines(L)
                            cs.target_object = None #REMOVE IN ACTUAL OPERATION
                    else:
                        L = "Chosen Object of type " + str(cs.target_object.kind) + " has been lost.\r"
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

def test3():
    file1 = open("./ListE/ResultsE.txt", "w")
    tests_passed = 0
    for i in range(test_amount):
        file1.writelines("#### Test " + str(i) + " ####\r")
        cs.object_priority = [1,3,4,5,2]
        cs.frame_objects = []
        cs.target_object = None

        ss.INPUT_FILE = "./ListE/CurrentFrame" + str(i) + ".csv"
        file1.writelines("# CurrentFrame" + str(i) + ".csv\r")

        while cs.object_priority:
            cs.frame_objects = ss.get_objects()
            if cs.target_object:
                if cs.check_target_in_frame():
                    if cs.check_investigated():
                        cs.object_priority.remove(cs.target_object.kind)
                        L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                        file1.writelines(L)
                        cs.target_object = None
                    else:
                        cs.object_priority.remove(cs.target_object.kind) #REMOVE IN ACTUAL OPERATION
                        L = "Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                        file1.writelines(L)
                        cs.target_object = None #REMOVE IN ACTUAL OPERATION
                else:
                    L = "Chosen Object of type " + str(cs.target_object.kind) + " has been lost.\r"
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
                
        if cs.object_priority:
            ss.INPUT_FILE = "./ListE/NextFrame" + str(i) + ".csv"
            file1.writelines("# NextFrame" + str(i) + ".csv\r")

            while cs.object_priority:
                cs.frame_objects = ss.get_objects()
                if cs.target_object:
                    if cs.check_target_in_frame():
                        if cs.check_investigated():
                            cs.object_priority.remove(cs.target_object.kind)
                            L = "(Actually Investigated) Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                            file1.writelines(L)
                            cs.target_object = None
                        else:
                            cs.object_priority.remove(cs.target_object.kind) #REMOVE IN ACTUAL OPERATION
                            L = "Chosen Object Type: " + str(cs.target_object.kind) + "\r"
                            file1.writelines(L)
                            cs.target_object = None #REMOVE IN ACTUAL OPERATION
                    else:
                        L = "Chosen Object of type " + str(cs.target_object.kind) + " has been lost.\r"
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
    test3_2_1()
    test3()
