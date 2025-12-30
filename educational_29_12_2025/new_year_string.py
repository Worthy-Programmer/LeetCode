'''
Docstring for educational_29_12_2025.new_year_string
https://codeforces.com/contest/2182/problem/A
'''

import math 
import sys



def is_new_year(haystack: str):
    return haystack.find('2026') >= 0  or haystack.find('2025') < 0

def update_string(string, char, index):
    l = list(string)
    l[index] = char
    return str(l)

def edit(n, string, index): # DP - Typical edit distance problem
    if is_new_year(string): return n
    if index >= len(string): return math.inf
    prev = index - 1 

    edit_d = math.inf
    if prev == -1 or string[prev] in [0, 6, 5]:
        edit_d = edit(n+1, update_string(string, '2', index), index+1)

    if string[prev] == 2:
        edit_d_1 = edit(n+1, update_string(string, '0', index), index + 1)
        edit_d_2 = edit(n+1, update_string(string, '6', index),  index + 1)
        edit_d = min(edit_d_1, edit_d_2)

    skip_d = edit(n+1, string, index+1)

    return min(edit_d, skip_d)

def read():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        sys.stdin.readline()
        line = sys.stdin.readline().strip()
        print(edit(0, line, 0))
    
read()