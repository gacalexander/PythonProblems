

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


    return "No Result"

import random
import numpy as np


def test_check_ttt():
    test_game_random = [[0,0,0] for elem in range(3)]
    boxes_filled = random.randint(0,8)
    num_circles = int(boxes_filled/2)

    circle_ind = random.sample(range(9),num_circles)
    cross_ind = random.sample([elem for elem in range(9) if elem not in circle_ind],(boxes_filled-num_circles))        

    for elem in circle_ind: test_game_random[int(elem/3)][elem%3] = 1
    for elem in cross_ind: test_game_random[int(elem/3)][elem%3] = -1
    print(np.array(test_game_random))
    print("\nYour Result: {}".format(check_ttt(test_game_random)))

    your_answer = check_ttt(test_game_random)
    if 3 in np.sum(test_game_random,axis=0) and -3 in np.sum(test_game_random,axis=0): pass
    elif 3 in np.sum(test_game_random,axis=1) and -3 in np.sum(test_game_random,axis=1): pass
    elif 3 in np.sum(test_game_random,axis=0) and -3 in np.sum(test_game_random,axis=1): pass
    elif 3 in np.sum(test_game_random,axis=1) and -3 in np.sum(test_game_random,axis=0): pass
    elif 3 in np.sum(test_game_random,axis=0): assert your_answer == "Circles (+1) Win"
    elif -3 in np.sum(test_game_random,axis=0): assert your_answer == "Crosses (-1) Win"
    elif 3 in np.sum(test_game_random,axis=1): assert your_answer == "Circles (+1) Win"
    elif -3 in np.sum(test_game_random,axis=1): assert your_answer == "Crosses (-1) Win"
    elif np.trace(test_game_random) == 3: assert your_answer == "Circles (+1) Win"
    elif np.trace(test_game_random) == -3: assert your_answer == "Crosses (-1) Win"
    elif np.flipud(test_game_random).trace() == 3: assert your_answer == "Circles (+1) Win"
    elif np.flipud(test_game_random).trace() == -3: assert your_answer == "Crosses (-1) Win"
    else: assert check_ttt(test_game_random) == "No Result"

print("testing function for random game states..")
for i in range(20):
    print("---------- Game State {} ----------".format(i))
    test_check_ttt()

print("\n(Passed!)")


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


