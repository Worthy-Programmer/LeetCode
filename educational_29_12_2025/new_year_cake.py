'''
Docstring for educational_29_12_2025.new_year_cake

https://codeforces.com/contest/2182/problem/B
'''

import math
import sys

def find_layers(a, b):
    a,b = min(a,b), max(a,b)    
    n_even, n_odd  = find_n_even(a,b), find_n_odd(a,b)
    return(max(n_even, n_odd))


def find_n_even(a,b):
    if (2*a < b): # In GP you will find out, b should be atleast 2a
        b = 2* a
    else:
        a = b//2

    h = math.floor(math.log( 3 *a + 1 , 4)) # From GP Sum expression: a=  (4^h - 1 ) / (4-1)
    n_even =  2 * h
    return n_even

def find_n_odd(a,b):
    
    h = math.floor(math.log(1.5*a + 1, 4))  # From GP Sum expression: b=  2(4^(h+1) - 1 ) / (4-1)
    expected_b = int((4**(h+1) - 1 ) / 3) # From GP Sum expression: b=  (4^h - 1 ) / (4-1)

    if expected_b <= b:
        return 2*h + 1 
    return 2 *h - 1 # If there is not enough b, print the previous odd number

def read():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        line = sys.stdin.readline().strip()
        a,b = list(map(int, line.split()))
        print(find_layers(a,b))
    
read()
    

    


