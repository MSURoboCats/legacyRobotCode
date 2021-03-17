import random as rd
import os
import errno

### ASSUMING BOTTOM LEFT IS 0,0 ###
### OBJECT OVERLAP NOT ACCOUNTED FOR ###

#---------------------------------------------------------------
# Shift All Objects Random Directions
#---------------------------------------------------------------
def list_D(num_tests):

    max_objects = 5
    min_object_dimension = 20

    #---------------------------------------------------------------
    # Make "ListD" folder to place data into
    #---------------------------------------------------------------
    filename = "./ListD/"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    #---------------------------------------------------------------
    # Make 2 Sequential CSVs
    #---------------------------------------------------------------
    for j in range(num_tests):
        oneTypeOfEach = []
        rows = rd.randint(0,max_objects) # Number of objects in CSV
        f = open(filename + "CurrentFrame" + str(j) + ".csv", "w")
        g = open(filename + "NextFrame" + str(j) + ".csv", "w")
        for i in range(rows):
            loop = 1
            #---------------------------------------------------------------
            # Calculate Original Variables
            #---------------------------------------------------------------
            #---------- Original Centroids ----------
            xc = rd.randint(min_object_dimension/2,(1280 - min_object_dimension/2))
            yc = rd.randint(min_object_dimension/2,(720 - min_object_dimension/2))

            #---------- Get xd ----------
            if (1280 - xc) <= xc:
                xd = rd.randint(min_object_dimension,2*(1280 - xc))
            else:
                xd = rd.randint(min_object_dimension,2*xc)
                
            #---------- Get yd ----------    
            if (720 - yc) <= yc:
                yd = rd.randint(min_object_dimension,2*(720 - yc))
            else:
                yd = rd.randint(min_object_dimension,2*yc)

            #---------------------------------------------------------------
            # Calculate Shifted Variables
            #---------------------------------------------------------------
            #---------- Shifted Centroids ----------
            xcs = xc + rd.randint(-50,50)
            ycs = yc + rd.randint(-50,50)

            #---------- Get xds ----------
            if xcs + xd/2 > 1280:  # If object is not entirely in frame (Off the RIGHT side of frame)
                xds = int(xd - ((xcs + xd/2) - 1280))  # Update xd with lost dimension removed.
                xcs = int(1280 - xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif xcs - xd/2 < 0:  # If object is not entirely in frame (Off the LEFT side of frame)
                xds = int(xd - abs(xcs - xd/2))  # Update xd with lost dimension removed.
                xcs = int(xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                xds = xd

            #---------- Get yds ----------
            if ycs + yd/2 > 720:  # If object is not entirely in frame (Off the TOP of frame)
                yds = int(yd - ((ycs + yd/2) - 720))  # Update xyd with lost dimension removed.
                ycs = int(720 - yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif ycs - yd/2 < 0:  # If object is not entirely in frame (Off the BOTTOM of frame)
                yds = int(yd - abs(ycs - yd/2))  # Update yd with lost dimension removed.
                ycs = int(yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                yds = yd
                
            #---------------------------------------------------------------
            # Create 2 CSV
            #---------------------------------------------------------------
            while loop == 1:
                type = rd.randint(1,max_objects)
                if oneTypeOfEach.count(type) == 0: # Only one of each object type
                    f.write(str(xc) + "," + str(yc) + "," + str(xd) + "," + str(yd) + "," + str(type) + "\r")  # First CSV
                    g.write(str(xcs) + "," + str(ycs) + "," + str(xds) + "," + str(yds) + "," + str(type) + "\r")  # Shifted CSV
                    oneTypeOfEach.append(type)
                    loop = 0
        f.close()
        g.close()

#---------------------------------------------------------------
# Shift All Objects The Same Direction
#---------------------------------------------------------------
def list_E(num_tests):

    max_objects = 5
    min_object_dimension = 20
    xshift = rd.randint(-50,50)
    yshift = rd.randint(-50,50)

    #---------------------------------------------------------------
    # Make "ListE" folder to place data into
    #---------------------------------------------------------------
    filename = "./ListE/"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    #---------------------------------------------------------------
    # Make 2 Sequential CSVs
    #---------------------------------------------------------------
    for j in range(num_tests):
        oneTypeOfEach = []
        rows = rd.randint(0,max_objects) # Number of objects in CSV
        f = open(filename + "CurrentFrame" + str(j) + ".csv", "w")
        g = open(filename + "NextFrame" + str(j) + ".csv", "w")
        for i in range(rows):
            loop = 1
            #---------------------------------------------------------------
            # Calculate Original Variables
            #---------------------------------------------------------------
            #---------- Original Centroids ----------
            xc = rd.randint(min_object_dimension/2,(1280 - min_object_dimension/2))
            yc = rd.randint(min_object_dimension/2,(720 - min_object_dimension/2))

            #---------- Get xd ----------
            if (1280 - xc) <= xc:
                xd = rd.randint(min_object_dimension,2*(1280 - xc))
            else:
                xd = rd.randint(min_object_dimension,2*xc)
                
            #---------- Get yd ----------    
            if (720 - yc) <= yc:
                yd = rd.randint(min_object_dimension,2*(720 - yc))
            else:
                yd = rd.randint(min_object_dimension,2*yc)

            #---------------------------------------------------------------
            # Calculate Shifted Variables
            #---------------------------------------------------------------
            #---------- Shifted Centroids ----------
            xcs = xc + xshift  # Move centroids toward center by half the distance.
            ycs = yc + yshift
                
            #---------- Get xds ----------
            if xcs + xd/2 > 1280:  # If object is not entirely in frame (Off the RIGHT side of frame)
                xds = int(xd - ((xcs + xd/2) - 1280))  # Update xd with lost dimension removed.
                xcs = int(1280 - xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif xcs - xd/2 < 0:  # If object is not entirely in frame (Off the LEFT side of frame)
                xds = int(xd - abs(xcs - xd/2))  # Update xd with lost dimension removed.
                xcs = int(xds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                xds = xd

            #---------- Get yds ----------
            if ycs + yd/2 > 720:  # If object is not entirely in frame (Off the TOP of frame)
                yds = int(yd - ((ycs + yd/2) - 720))  # Update xyd with lost dimension removed.
                ycs = int(720 - yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
                
            elif ycs - yd/2 < 0:  # If object is not entirely in frame (Off the BOTTOM of frame)
                yds = int(yd - abs(ycs - yd/2))  # Update yd with lost dimension removed.
                ycs = int(yds/2)  # Centroid is also slightly moved when dimensions are cuttoff
            else:  # Not cutoff
                yds = yd
                
            #---------------------------------------------------------------
            # Create 2 CSV
            #---------------------------------------------------------------
            while loop == 1:
                type = rd.randint(1,max_objects)
                if oneTypeOfEach.count(type) == 0: # Only one of each object type
                    f.write(str(xc) + "," + str(yc) + "," + str(xd) + "," + str(yd) + "," + str(type) + "\r")  # First CSV
                    g.write(str(xcs) + "," + str(ycs) + "," + str(xds) + "," + str(yds) + "," + str(type) + "\r")  # Shifted CSV
                    oneTypeOfEach.append(type)
                    loop = 0
        f.close()
        g.close()


##### CALLING THE FUNCTIONS #####
        
list_D(50) # How many cases? (Generates 2 CSVs per case)
list_E(50) # How many cases? (Generates 2 CSVs per case)
