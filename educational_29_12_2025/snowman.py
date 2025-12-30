'''
Docstring for educational_29_12_2025.snowman
https://codeforces.com/contest/2182/problem/C

Combinatorics - used AI help

Idea:
Answer = n x valid_shift_AB x valid_shift_BC

A < B and B < C are independent. So I don't have to see all three together
'''
import sys

def find_indices(n, a, b, c):
    return n * find_valid_shifts(n,a,b) * find_valid_shifts(n, b, c)
    

# O (n^2)
def find_valid_shifts(n, a, b):
    extended_b = b * 2
    valid_count = 0
    for k in range(n):  # k = shifts
        is_valid = True
        for i in range(n):
            if a[i] >= extended_b[k+i]:
                is_valid = False
                break
        if is_valid:valid_count +=1 
    return valid_count
    
def rl():
    return sys.stdin.readline().strip()
def read():
    no_of_questions = int(sys.stdin.readline())

    for i in range(no_of_questions):
        n = int(rl())
        containers= []
        for j in range(3):
            a = list(map(int, rl().split()))
            containers.append(a)
        print(find_indices(n, *containers))

read()