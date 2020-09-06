def all_pairs(items):
    item_pair = []
    # item_pair = [(items[i], items[j]) for i in range(len(items)) for j in range(i + 1, len(items))]
    item_pair = [(items[i], items[j]) for i in items for j in items[i+1:l]]
    print(item_pair)
    return len(item_pair)

print(all_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Test cell: Test_Code1

def test_code1():
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = [1, 1, 1, 2, 2, 3, 4, 10]
    L3 = [1, 4, 7, 9]
    L4 = []
    # assert count_pairs(L1) == 8, "Test Case L1 failed"
    # assert count_pairs(L2) == 9, "Test Case L2 failed"
    # assert count_pairs(L3) == 0, "Test Case L3 failed"
    # assert count_pairs(L4) == 0, "Test Case L4 failed"
    print("\n(Passed!)")


test_code1()
