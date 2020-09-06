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


