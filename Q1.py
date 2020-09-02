# Assignment 4 Question 1
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

#add in more test cases for your function
treasure_map1 = [[1,1,1,1,0,1],
                 [0,0,0,0,0,1],
                 [1,1,0,1,1,1],
                 [1,0,0,0,2,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1]]

# different entrance
treasure_map2 = [[0,0,1,1,0,1],
                 [1,0,0,0,0,1],
                 [1,1,0,1,1,1],
                 [1,0,0,0,2,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1]]

# might have no treasure
treasure_map3 = [[1,1,1,1,0,1],
                 [0,0,0,0,0,1],
                 [1,1,0,1,1,1],
                 [1,0,0,0,0,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1]]

# no path to treasure
treasure_map4 = [[0,0,1,1,0,1],
                 [1,0,0,0,0,1],
                 [1,1,0,1,1,1],
                 [1,0,0,1,2,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1]]

# treasure in first row
treasure_map5 = [[1,1,1,1,2,1],
                 [1,1,0,0,0,1],
                 [1,0,0,1,1,1],
                 [0,0,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1]]

#treasure in last row
treasure_map6 = [[0,0,1,1,1,1],
                 [1,0,0,0,1,1],
                 [1,1,1,0,1,1],
                 [1,1,1,0,1,1],
                 [1,1,1,0,0,1],
                 [1,1,1,1,2,1]]

#treasure in first column
treasure_map7 = [[0,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [2,0,1,1,1,1],
                 [1,1,1,1,1,1]]

#treasure in last column
treasure_map8 = [[0,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [1,0,1,1,1,1],
                 [1,0,0,0,0,2],
                 [1,1,1,1,1,1]]

#treasure in first row, last column
treasure_map9 = [[1,1,1,1,1,2],
                 [1,1,1,0,0,0],
                 [1,1,0,0,1,1],
                 [1,0,0,1,1,1],
                 [0,0,1,1,1,1],
                 [1,1,1,1,1,1]]

#treasure in last row, last column
treasure_map10 = [[1,1,1,1,1,1],
                  [0,0,0,1,1,1],
                  [1,1,0,0,1,1],
                  [1,1,1,0,1,1],
                  [1,1,1,0,1,1],
                  [1,1,1,0,0,2]]

#treasure in first row, first column
treasure_map11 = [[2,0,1,1,1,1],
                  [1,0,1,1,1,1],
                  [1,0,1,1,1,1],
                  [0,0,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1]]

#treasure in last row, first column
treasure_map12 = [[1,1,1,1,1,1],
                  [0,0,1,1,1,1],
                  [1,0,1,1,1,1],
                  [1,0,1,1,1,1],
                  [1,0,1,1,1,1],
                  [2,0,1,1,1,1]]
# map size check
treasure_map13= [[0,0,0,1],
                 [1,0,0,0,0]]

treasure_map14= [[0,0,0,1]]

def get_map_size(treasure_map):
    # m is row
    # n is col
    m = len(treasure_map)
    n = len(treasure_map[0])
    size_of_map = [m,n]
    return size_of_map
   
# find coordinates of starting location
def find_entrance_location(treasure_map):
    entrance_location_coord = []
    for row in range(len(treasure_map)):     
        # check every row & col
        for col in range(len(treasure_map[row])):
            entrance_location_value = treasure_map[row][col]
            # assume: entrance is always in first column
            if (col == 0):
                # assume: only 1 entrance
                if (entrance_location_value == 0):
                    entrance_location_coord = [row,col]
                
    return entrance_location_coord    
            
# check if
def check_treasure_exist(treasure_map):
    # check if there is treasure 
    treasure_exist = False
    # loop through all rows
    for row in range(len(treasure_map)):     
        # check every row & col
        for col in range(len(treasure_map[row])):
            treasure_location_value = treasure_map[row][col]
            # assume: only 1 treasure
            if(treasure_location_value == 2):
                treasure_exist = True
        
    return treasure_exist

# find coordinates of treasure location
def find_treasure_location(treasure_map):
    treasure_location_coord = []
    for row in range(len(treasure_map)):     
        # check every row & col
        for col in range(len(treasure_map[row])):
            treasure_location_value = treasure_map[row][col]
            if(treasure_location_value == 2):
                treasure_location_coord = [row,col]  
    return treasure_location_coord

#check if
#if true means up_location of treasure does not exist
def treasure_location_in_first_row(treasure_map):
    first_row = True
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    if (row_location == 0):
        first_row = True
    else:
        first_row = False
    return first_row

#check if
#if true means down_location of treasure does not exist
def treasure_location_in_last_row(treasure_map):
    last_row = True
    #get m size
    row_max_size = get_map_size(treasure_map)[0]-1    
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    if (row_location == row_max_size):
        last_row = True
    else:
        last_row = False
    return last_row

#check if
#if true means left_location of treasure does not exist
def treasure_location_in_first_column(treasure_map):
    first_column = True
    treasure_location = find_treasure_location(treasure_map)
    column_location = treasure_location[1]
    if(column_location == 0):
        first_column = True
    else:
        first_column = False
    return first_column

#check if  
#if true means right_location of treasure does not exist
def treasure_location_in_last_column(treasure_map):
    last_column = True
    #get n size
    col_max_size = get_map_size(treasure_map)[1]-1
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    column_location = treasure_location[1]
    if (column_location == col_max_size):
        last_column = True
    else:
        last_column = False
    return last_column

def find_left_location_of_treasure(treasure_map):
    left_of_treasure = []
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    column_location = treasure_location[1]
    if(not(treasure_location_in_first_column(treasure_map))):
        left_of_treasure = [row_location,column_location-1]
    return left_of_treasure

def find_right_location_of_treasure(treasure_map):
    right_of_treasure = []
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    column_location = treasure_location[1]
    if(not(treasure_location_in_last_column(treasure_map))):
        right_of_treasure = [row_location,column_location+1]
    return right_of_treasure

def find_up_location_of_treasure(treasure_map):
    up_of_treasure = []
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    column_location = treasure_location[1]
    if(not(treasure_location_in_first_row(treasure_map))):
        up_of_treasure = [row_location-1,column_location]
    return up_of_treasure

def find_down_location_of_treasure(treasure_map):
    down_of_treasure = []
    treasure_location = find_treasure_location(treasure_map)
    row_location = treasure_location[0]
    column_location = treasure_location[1]
    if(not(treasure_location_in_last_row(treasure_map))):
        down_of_treasure = [row_location+1,column_location]
    return down_of_treasure

#check if there is a path
def find_treasure_path_exist(treasure_map): 
    # assign locations of left, right, up, down of treasure
    left_location = find_left_location_of_treasure(treasure_map)
    right_location = find_right_location_of_treasure(treasure_map)
    up_location = find_up_location_of_treasure(treasure_map)
    down_location = find_down_location_of_treasure(treasure_map)
    
    path_exist = False
    check_count = 0
    # check treasure's surrounding up,down,left,right locations
    # as long as there's a 0 on either up,down,left,right 
    # there is a path
    for row in range(len(treasure_map)):     
        for col in range(len(treasure_map[row])):
            #in left location, check left value
            if ([row,col] == left_location):
                val_of_left = treasure_map[row][col]
                if (val_of_left == 0):
                    check_count = check_count + 1
            #in right location, check right value
            elif([row,col] == right_location):
                val_of_right = treasure_map[row][col]            
                if (val_of_right == 0):
                    check_count = check_count + 1                
            #in up location, check up value
            elif([row,col] == up_location):
                val_of_up = treasure_map[row][col]  
                if (val_of_up == 0):
                    check_count = check_count + 1                    
            #in down location, check up value
            elif([row,col] == down_location):
                val_of_down = treasure_map[row][col]
                if (val_of_down == 0):
                    check_count = check_count + 1                
    if (check_count > 0):
        path_exist = True                
    else:
        path_exist = False
    return path_exist

#general up, down, left, right steps
def up_step(coordinate):
    up_step_coord = []
    row = coordinate[0]
    col = coordinate[1]
    if (row-1 >=0):
        up_step_coord = [row-1,col]
    return up_step_coord

def down_step(coordinate, treasure_map):
    down_step_coord = []
    row = coordinate[0]
    col = coordinate[1]
    if (row <= get_map_size(treasure_map)[0]):
        down_step_coord = [row+1, col]
    return down_step_coord

def left_step(coordinate):
    left_step_coord = []
    row = coordinate[0]
    col = coordinate[1]
    if(col-1>=0):
        left_step_coord = [row, col-1]
    return left_step_coord

def right_step(coordinate, treasure_map):
    right_step_coord = []
    row = coordinate[0]
    col = coordinate[1]
    if(col <= get_map_size(treasure_map)[1]):
        right_step_coord = [row, col+1]
    return right_step_coord

#finds next step coordinates
def next_step(coordinate, treasure_map, all_path):
    next_step_coord = []
    
    left_location = left_step(coordinate)
    right_location = right_step(coordinate, treasure_map)
    up_location = up_step(coordinate)
    down_location = down_step(coordinate, treasure_map)
    
    treasure_location = find_treasure_location(treasure_map)
    
    # other steps up to treasure location
    if all_path:
        prev_location = all_path[len(all_path)-1-1]
        if (prev_location == left_location):
            for row in range(len(treasure_map)):     
                for col in range(len(treasure_map[row])):
                    #in right location, check right value
                    if([row,col] == right_location):
                        val_of_right= treasure_map[row][col]
                        #possible moving space
                        if (val_of_right == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_right == 2):
                            next_step_coord = treasure_location                
                    #in up location, check up value
                    elif([row,col] == up_location):
                        val_of_up= treasure_map[row][col]
                        #possible moving space
                        if (val_of_up == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_up == 2):
                            next_step_coord = treasure_location                  
                    #in down location, check up value
                    elif([row,col] == down_location):
                        val_of_down= treasure_map[row][col]
                        #possible moving space
                        if (val_of_down == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_down == 2):
                            next_step_coord = treasure_location
        elif (prev_location == right_location):
            for row in range(len(treasure_map)):     
                for col in range(len(treasure_map[row])):
                    #in left location, check left value
                    if ([row,col] == left_location):
                        val_of_left = treasure_map[row][col]
                        #possible moving space
                        if (val_of_left == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_left == 2):
                            next_step_coord = treasure_location              
                    #in up location, check up value
                    elif([row,col] == up_location):
                        val_of_up= treasure_map[row][col]
                        #possible moving space
                        if (val_of_up == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_up == 2):
                            next_step_coord = treasure_location                  
                    #in down location, check up value
                    elif([row,col] == down_location):
                        val_of_down= treasure_map[row][col]
                        #possible moving space
                        if (val_of_down == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_down == 2):
                            next_step_coord = treasure_location            
        elif (prev_location == up_location):
            for row in range(len(treasure_map)):     
                for col in range(len(treasure_map[row])):
                    #in left location, check left value            
                    if ([row,col] == left_location):
                        val_of_left = treasure_map[row][col]
                        #possible moving space
                        if (val_of_left == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_left == 2):
                            next_step_coord = treasure_location
                    #in right location, check right value
                    elif([row,col] == right_location):
                        val_of_right= treasure_map[row][col]
                        #possible moving space
                        if (val_of_right == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_right == 2):
                            next_step_coord = treasure_location                                 
                    #in down location, check up value
                    elif([row,col] == down_location):
                        val_of_down= treasure_map[row][col]
                        #possible moving space
                        if (val_of_down == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_down == 2):
                            next_step_coord = treasure_location           
        elif (prev_location == down_location):
            for row in range(len(treasure_map)):     
                for col in range(len(treasure_map[row])):
                    #in left location, check left value
                    if ([row,col] == left_location):
                        val_of_left = treasure_map[row][col]
                        #possible moving space
                        if (val_of_left == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_left == 2):
                            next_step_coord = treasure_location
                    #in right location, check right value
                    elif([row,col] == right_location):
                        val_of_right= treasure_map[row][col]
                        #possible moving space
                        if (val_of_right == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_right == 2):
                            next_step_coord = treasure_location                
                    #in up location, check up value
                    elif([row,col] == up_location):
                        val_of_up= treasure_map[row][col]
                        #possible moving space
                        if (val_of_up == 0):
                            next_step_coord = [row,col]
                        #treasure location
                        elif (val_of_up == 2):
                            next_step_coord = treasure_location                 
    #only for starting step
    else:
        for row in range(len(treasure_map)):     
            for col in range(len(treasure_map[row])):
                #in left location, check left value
                if ([row,col] == left_location):
                    val_of_left = treasure_map[row][col]
                    #possible moving space
                    if (val_of_left == 0):
                        next_step_coord = [row,col]
                    #treasure location
                    elif (val_of_left == 2):
                        next_step_coord = treasure_location
                #in right location, check right value
                elif([row,col] == right_location):
                    val_of_right= treasure_map[row][col]
                    #possible moving space
                    if (val_of_right == 0):
                        next_step_coord = [row,col]
                    #treasure location
                    elif (val_of_right == 2):
                        next_step_coord = treasure_location                
                #in up location, check up value
                elif([row,col] == up_location):
                    val_of_up= treasure_map[row][col]
                    #possible moving space
                    if (val_of_up == 0):
                        next_step_coord = [row,col]
                    #treasure location
                    elif (val_of_up == 2):
                        next_step_coord = treasure_location                  
                #in down location, check up value
                elif([row,col] == down_location):
                    val_of_down= treasure_map[row][col]
                    #possible moving space
                    if (val_of_down == 0):
                        next_step_coord = [row,col]
                    #treasure location
                    elif (val_of_down == 2):
                        next_step_coord = treasure_location
                        
    return next_step_coord 

def store_all_paths(treasure_map):
    all_path = []
    
    #starting location
    entrance_location = find_entrance_location(treasure_map)
    #find next step location from starting location
    next_step_location = next_step(entrance_location,treasure_map,all_path)

    #put inside a list
    all_path.append(entrance_location)
    all_path.append(next_step_location)

    treasure_location = find_treasure_location(treasure_map)

    # find full path until treasure
    i = 0
    while treasure_location not in all_path:
        i =  i + 1
        all_path.append(next_step(all_path[i],treasure_map,all_path))          
        
    return all_path

#Code this function find_treasure(treasure_map)
#This function should be stand alone and should not use another other global variables declared outside the function
def find_treasure(treasure_map):
    
    path = {}
    
    # check map size
    mapsize = get_map_size(treasure_map)
    if (mapsize[0] < 5 or mapsize[1] < 5):    
        path = {'e':'Map size cannot be smaller than 5'}
    elif (mapsize[0] < 5 and mapsize[1] < 5):
        path = {'e':'Map size cannot be smaller than 5'}
    else:
        # check if there is treasure
        #if no treasure break and print error
        if (not(check_treasure_exist(treasure_map))):
            path = {'e':'No treasure found in the map'}
        #else there is treasure
        else:
            #if treasure exist
            # check if path exist
            # if path don't exist throw error
            if(not(find_treasure_path_exist(treasure_map))):
                path = {'e':'No possible path to treasure in the map'}
            else:
                path_list = []
                path_list = store_all_paths(treasure_map)
                    
                row_path_list = [path[0] for path in path_list]
                col_path_list = [path[1] for path in path_list]
                
                # r is row, c is column                
                for i in range(len(path_list)):
                    path.setdefault(i+1, {})['r'] = row_path_list[i]
                    path.setdefault(i+1, {})['c'] = col_path_list[i]           
    return path

def main():
    path = find_treasure(treasure_map1)
    #path = find_treasure(treasure_map2)
    
    #no treasure found:
    #path = find_treasure(treasure_map3)
    
    #no possible path:
    #path = find_treasure(treasure_map4)
    
    #path = find_treasure(treasure_map5)
    #path = find_treasure(treasure_map6)
    #path = find_treasure(treasure_map7)
    #path = find_treasure(treasure_map8)
    #path = find_treasure(treasure_map9)
    #path = find_treasure(treasure_map10)
    #path = find_treasure(treasure_map11)
    #path = find_treasure(treasure_map12)
    #path = find_treasure(treasure_map13)
    #path = find_treasure(treasure_map14)

    for step in path:
        print(path.get(step))
    
main()


