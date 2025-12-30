'''
Docstring for educational_29_12_2025.tree_decoration

https://codeforces.com/contest/2182/problem/D
Combinatorics question
'''

import sys
import math
import io

f = sys.stdin

def rl():
    global f
    return f.readline().strip()

def read():
    q = int(rl())

    for i in range(q):
        n = int(rl())
        boxes = list(map(int, rl().split()))
        print(find_permutations(n, boxes))

def is_correct(boxes):
    for i in range(1, len(boxes)):
        if(not boxes[i] == boxes[0] -1): return False
    return True

def find_permutations(n, boxes): # O(nlogn + box_zero - n)
    least = min(boxes)
    if least != 0:
        for i in range(1, n + 1):
            boxes[i] -= least

    box_0 = int(boxes[0])
    boxes = sorted(boxes[1:], reverse=True) # o(nlogn)
    # print(boxes)

    for i in range(1, n):
        left = max(boxes[0] -1 - boxes[i], 0)
        to_be_added = min(box_0, left)
        boxes[i] += to_be_added

        box_0 -= to_be_added

        if (box_0 <=0 ): break

    if not is_correct(boxes): return 0

    p = math.factorial (n-1)

    # print('Initial p', p, boxes)
 
    if box_0 > 0: 
        for i in range(box_0):
            boxes[ (1+i) % n ] += 1

    same_number_as_first = 0
    for box_n in boxes:
        if box_n != boxes[0]: break
        same_number_as_first += 1

    p *= math.factorial(same_number_as_first)

    return p%998244353


f = io.StringIO("4\n3\n1 2 1 0\n3\n1 0 2 0\n1\n2 5\n4\n6 1 4 2 1\n")

read()
