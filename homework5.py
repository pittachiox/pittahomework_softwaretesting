#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Sort each row in the grid
    sorted_rows = [''.join(sorted(row)) for row in grid]
    
    # Check if columns are sorted
    for col in range(len(sorted_rows[0]) if sorted_rows else 0):
        for row in range(1, len(sorted_rows)):
            if sorted_rows[row][col] < sorted_rows[row - 1][col]:
                return 'NO'
    return 'YES'


def test_gridChallenge():
    # Test Case 1
    grid1 = ["abc", "def", "ghi"]
    assert gridChallenge(grid1) == "YES", "Test Case 1 Failed"

    # Test Case 2
    grid2 = ["cab", "fde", "igh"]
    assert gridChallenge(grid2) == "YES", "Test Case 2 Failed"

    # Test Case 3
    grid3 = ["cab", "fde", "igc"]
    assert gridChallenge(grid3) == "NO", "Test Case 3 Failed"

    # Test Case 4
    grid4 = ["a"]
    assert gridChallenge(grid4) == "YES", "Test Case 4 Failed"

    # Test Case 5
    grid5 = ["ebac", "fghd", "olmn", "pqrs"]
    assert gridChallenge(grid5) == "YES", "Test Case 5 Failed"

    # Test Case 6
    grid6 = []
    assert gridChallenge(grid6) == "YES", "Test Case 6 Failed"

    # Test Case 7
    grid7 = ["aab", "bba", "ccc"]
    assert gridChallenge(grid7) == "YES", "Test Case 7 Failed"

    # Test Case 8
    grid8 = ["zyx", "wvu", "tsr"]
    assert gridChallenge(grid8) == "NO", "Test Case 8 Failed"

    print("All test cases passed!")


if __name__ == '__main__':
    # รันการทดสอบ
    test_gridChallenge()

    # หากต้องการรันโค้ดหลัก (อ่าน input จากไฟล์และเขียนผลลัพธ์)
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()