import csv
import numpy as np

GRID_HEIGHT = 15
WALKING_DISTANCE = 20
CAPACITY = 25
# with open('sample_data_bobstan.csv', newline='') as csvfile:
#     data = csv.reader(csvfile)
#     student_loc = np.array([])
#     school_loc = np.array([])
#     school_latitude = 0
#     school_longitude = 0
#     for row in data:
#         student_latitude = row[3]
#         student_longitude = row[4]
#         school_latitude = row[-2]
#         school_longitude = row[-1]
#         student_loc = np.append(student_loc,[student_latitude,student_longitude]) 
#     school_loc = np.append(school_loc,[school_latitude,school_longitude])
#     student_loc = student_loc.reshape(student_loc.size//2, 2)
#     school_loc = school_loc.astype(np.float)
#     student_loc = student_loc.astype(np.float)

#     # normalize the data
#     temp_min = student_loc.min(axis=0)
#     student_loc -= temp_min
#     school_loc -= temp_min
#     student_loc = student_loc*1000
#     school_loc = school_loc*1000
#     student_loc = student_loc.astype(int)
#     school_loc = school_loc.astype(int)

#     increment_x = student_loc.max(axis=0)[0] / GRID_HEIGHT
#     GRID_WIDTH = int(student_loc.max(axis=0)[1]/ increment_x)

#     # print general information
#     print("%d stops, %d students, %.2f maximum walk, %d capacity" % (GRID_WIDTH*GRID_HEIGHT+1, len(student_loc), WALKING_DISTANCE, CAPACITY) )

#     # print the school location
#     print(0, school_loc[0], school_loc[1])
#     # print the final potential bus stop location
#     counter = 0
#     increment_x = student_loc.max(axis=0)[0] / GRID_HEIGHT
#     GRID_WIDTH = int(student_loc.max(axis=0)[1]/ increment_x)
#     for i in range(GRID_HEIGHT):
#         for j in range(GRID_WIDTH):
#             counter += 1
#             print("%d %d %d" % (counter,int(increment_x*i), int(increment_x*j)))
#     print("\n")
#     # print the students location
#     # sampled_data = student_loc[np.random.choice(student_loc.shape[0], 50, replace=False)]
#     sampled_data = student_loc
#     for i in range(len(sampled_data)):
#         print(i+1, sampled_data[i][0], sampled_data[i][1])


with open('sb1.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    student_loc = np.array([])
    school_loc = np.array([])
    school_latitude = 50
    school_longitude = 50
    for row in data:
        student_latitude = row[1]
        student_longitude = row[2]
        student_loc = np.append(student_loc,[student_latitude,student_longitude]) 
    school_loc = np.append(school_loc,[school_latitude,school_longitude])
    student_loc = student_loc.reshape(student_loc.size//2, 2)
    school_loc = school_loc.astype(np.float)
    student_loc = student_loc.astype(np.float)

    # normalize the data
    temp_min = student_loc.min(axis=0)
    student_loc -= temp_min
    school_loc -= temp_min
    student_loc = student_loc.astype(int)
    school_loc = school_loc.astype(int)

    increment_x = student_loc.max(axis=0)[0] / GRID_HEIGHT
    GRID_WIDTH = int(student_loc.max(axis=0)[1]/ increment_x)

    # print general information
    print("%d stops, %d students, %.2f maximum walk, %d capacity" % (GRID_WIDTH*GRID_HEIGHT+1, len(student_loc), WALKING_DISTANCE, CAPACITY) )

    # print the school location
    print(0, school_loc[0], school_loc[1])
    # print the final potential bus stop location
    counter = 0
    increment_x = student_loc.max(axis=0)[0] / GRID_HEIGHT
    GRID_WIDTH = int(student_loc.max(axis=0)[1]/ increment_x)
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            counter += 1
            print("%d %d %d" % (counter,int(increment_x*i), int(increment_x*j)))
    print("\n")
    # print the students location
    # sampled_data = student_loc[np.random.choice(student_loc.shape[0], 50, replace=False)]
    sampled_data = student_loc
    for i in range(len(sampled_data)):
        print(i+1, sampled_data[i][0], sampled_data[i][1])


