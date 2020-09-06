def check_ttt(game):
    assert len(game) ==3
    
    results = {
    0:"No Result",
    1:"Circles (+1) Win",
    2:"Crosses (-1) Win"
    }
    
    #Check diagnols
    diagfor = [0] * 3
    diagback = [0] * 3
    
    for row in range(0,3):
        diagfor[game[row][row]] += 1
        diagback[game[row][2-row]] += 1

    try:
        return results[diagfor.index(3)]
    except:
        pass


    try:
        return results[diagback.index(3)]
    except:
        pass


    #Checks Rows
    rowsums =[0]*3
    colsums =[0]*3

    #Check Row
    for row in range(0,3):
        rowsums =[0]*3
        for col in range(0,3):
             rowsums[game[row][col]]= rowsums[game[row][col]] + 1


        try:
            return results[rowsums.index(3)]
        except:
            pass



    #Check Cols
    for col in range(0,3):
        colsums =[0]*3
        for row in range(0,3):
            colsums[game[row][col]]= colsums[game[row][col]] + 1
        
        try:
            return results[colsums.index(3)]
        except:
            pass





# Test cell: test_cell_part0
import random
import numpy as np



# test 1
test_game1 = [[0,0,0] for elem in range(3)]
assert check_ttt(test_game1) == "No Result"

# santhis test 2
test_game2 = [[1,1,1],[1,-1,0],[1,0,0]]
assert check_ttt(test_game2) == "Circles (+1) Win"

# test 2
test_game2 = [[1,1,1],[-1,-1,0],[0,0,0]]
assert check_ttt(test_game2) == "Circles (+1) Win"

# test 3
test_game3 = [[0,0,-1],[1,-1,1],[-1,1,0]]
assert check_ttt(test_game3) == "Crosses (-1) Win"

# test 4
test_game4 = [[0,0,-1],[1,-1,-1],[1,1,-1]]
assert check_ttt(test_game4) == "Crosses (-1) Win"


print("\n(Passed!)")





'''
Exercise 3 (3 points). Now write a function get_route(segs, origin) that traces the complete itinerary of the pilot, given her first port of origin. Assume that the destination for a flight is the same as the origin for the next flight. The itinerary is completed when he arrives back at the starting port of origin. For example, if the starting port is "JFK", your function should return the list: ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"].
'''

segments = [("JFK", "DEN"), ("LAX", "ORD"), ("DEN", "SFO"), ("LAS", "LAX"), ("ORD", "ATL"), ("ATL", "JFK"), ("SFO", "LAS")]
start = "JFK"

import random
def get_route(path, origin):

    
    startSeg = [i[0] for i in segments]
    endSeg = [i[1] for i in segments]
    
    while endSeg != origin 
        print(startSeg)
        starSegIndex = startSeg.index(startPath))
        endSeg = endSeg[starSegIndex]
         print(startSeg,endSeg)
    
    if endSeg == origin:
        break
    
    
        
    
    
    while len(path) >= 1:
        current = None
        directions = {}

        for item in path:

            if item[0] == origin:
                directions[item[0]] = item[1]

        if len(directions) >= 1:
            current = min(directions.values())
            remove_tuple = (origin, current)

        try:
            path.remove(remove_tuple)
            if current != orig_start:
                itinerary_list.append(current)
                origin = current
        except:
            return "not valid intinerary"

    return itinerary_list

import random
# Test pilot route
ports = ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"]
starting_port = random.sample(ports, 5)
print(starting_port)
for p in starting_port:
     itinerary = get_route(segments, p)
     assert itinerary[0] == p, "incorrect port of origin for the itinerary"
     for i, port in enumerate(itinerary[:-1]):
         dest = find_dest(segments, port)
         print(dest)
         assert dest == itinerary[i+1], "incorrect itinerary"
print("\n(Passed.)")
