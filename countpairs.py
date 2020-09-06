'''
Exercise 0 (10 points). Given a list of integers, find the number of pairs that are consecutive.

For example, given the list, [1, 2, 5, 8]:

the pairs that can be formed from the given list are (1, 2), (1, 5), (1, 8), (2, 5), (2, 8), (5, 8);
the only pair that has consecutive integers is (1, 2) and hence the value to be returned is one (1).
If elements in the list are repeated, they should be treated as members of a distinct pair. For instance, if the list were [1, 1, 1, 2, 2, 5, 8, 8], then there are three ways to choose 1 and two ways to choose 2, or a total of  3×2=63×2=6  ways to choose the pair (1, 2), so that the answer would in this case be 6.

The first test case below tests for the correctness of the solution whereas the second one tests for the efficiency of the solution. That is, it should not take too long for the second case to pass! (To get "full credit," try to find a method that takes less than two (2) seconds on the test input of the second test.)

Application note. Although this might seem like a toy problem to solve, its application forms the basis of pattern recognition. For example, suppose you are trying to discover the buying pattern of products in a supermarket and want to figure out if placing two products next to each other impact each others' sales. (Does placing milk next to cereal drive both their sales upwards? Or if placing Muesli next to Cereal will lead to additional Muesli sales, since people who buy cereal would anyway buy Milk even if it is in the other corner of the store?)

In mapping that concrete placement problem into this abstract analysis problem, you can think of the list of numbers as the shelf numbers of products in a receipt, and you are trying to find out the number of cases where the products were in adjacent shelves.
'''
def count_pairs(items):    
    return len([(i, j) for i in items for j in items[i:] if j == i+1 ])

print(count_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Test cell: Test_Code1

def test_code1():
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = [1, 1, 1, 2, 2, 3, 4, 10]
    L3 = [1, 4, 7, 9]
    L4 = []
    assert count_pairs(L1) == 8, "Test Case L1 failed"
    assert count_pairs(L2) == 9, "Test Case L2 failed"
    # assert count_pairs(L3) == 0, "Test Case L3 failed"
    # assert count_pairs(L4) == 0, "Test Case L4 failed"
    print("\n(Passed!)")


test_code1()
